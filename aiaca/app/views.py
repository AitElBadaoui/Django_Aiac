import calendar

import datetime
import re
from decimal import Context, Decimal
import time
import pdfkit
from django.contrib.auth import authenticate, login, logout
import json
from django.db.models import Q, Sum
from django.template.loader import get_template
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from docx import Document
from docx.shared import Inches
from reportlab.lib.units import cm
from django.http import HttpResponse
from reportlab.pdfgen import canvas
# Create your views here.
from num2words import num2words
from xhtml2pdf import pisa

from app.forms import SeanceForm1, UserForm
from app.models import Semestre, Promotion, Semaine, Professeur, EmploiDuTemps, Matiere, Seance, Etudiant, \
    Horaire_semaine, Semaine_facture, Horaire_jour, User, Events

class set_mois(object):
    def __init__(self, mois, year):
        self.mois = mois
        self.year = year
    def __str__(self):
        return str(self.mois)
def check_authentification():
    user = User.objects.all()
    for a in user:
        a.is_verrou = False
        a.save()

def generate_emploi_archive():
    today = datetime.date.today()
    emploi = EmploiDuTemps.objects.filter(semaine__dateFin__lte=today)

    for i in emploi:
        i.isValid = True
        i.save()


def index(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
        else:
             return render(request, 'index.html')

#fonction qui permet de generer les semaines ainsi que les emploi du temps de chaque semestre :
def semestre_et_emploi_generation():
    today = datetime.date.today()
    semestre = Semestre.objects.filter(dateDebut__lte=today , dateFin__gte=today)
    for i in semestre:
        if i.is_full == 0:
            date_debut = i.dateDebut
            date_fin = i.dateFin
            num_semaine = 1
            monday = date_debut
            while monday <= date_fin:
                weekday = monday.weekday()
                start_delta = datetime.timedelta(days=weekday)
                start_of_week = monday - start_delta
                week_dates = [start_of_week + datetime.timedelta(days=i) for i in range(7)]
                if start_of_week < date_debut:
                    start_of_week = date_debut

                if week_dates[6] > date_fin:
                    week_dates[6] = date_fin

                if week_dates[6].isoweekday() != 7:
                    fin_emploi = week_dates[6]
                else:
                    fin_emploi = week_dates[5]

                semaine = Semaine(dateDebut=monday, dateFin=week_dates[6], semestre_id=i.id, num_semaine=num_semaine)
                semaine.save()
                emploi = EmploiDuTemps(semaine=semaine,dateDebut=monday,dateFin=fin_emploi,semestre=i)
                emploi.codeEmploi = emploi.code_Emploi()
                emploi.save()
                monday = week_dates[6] + datetime.timedelta(days=1)
                num_semaine += 1
            i.is_full = 1
            i.save()
    return 0

def count_seance(promotion):
    matiere = Matiere.objects.filter(semestre__promotion=promotion)
    for i in matiere:
        seance = Seance.objects.filter(matiere=i).count()
        i.seanceRealise = seance
        i.chargeRealise = seance * 3.5
        i.save()

#concerne les emplois du temps courant :
def emploi_du_temps_courant(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    semestre_et_emploi_generation()
    today = datetime.date.today()

    emploi = EmploiDuTemps.objects.filter(semaine__dateDebut__lte=today, semaine__dateFin__gte=today ,  isValid = False)
    context = {
        'emploi': emploi
    }

    return render(request, 'Emploi/Emploi_du_temps_courant.html', context)

def emploi_du_temps_courant_add(request , semestre , semaine , promotion):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    semestres = Semestre.objects.filter(libelle=semestre, promotion__libelle=promotion).first()
    emplois = EmploiDuTemps.objects.filter(semestre=semestres, semaine__num_semaine=semaine , isValid=False).first()

    if semestres and emplois:
        seance = Seance.objects.filter(emploi=emplois)
        url = "/emploi_du_temps/" + str(promotion) + "/" + str(semestre) + "/" + str(semaine)
        if request.method == "POST":
            seance = Seance.objects.filter(emploi=emplois)
            note = request.POST['note']
            if not seance:
                seance1 = SeanceForm1(request.POST, prefix='seance1')
                seance2 = SeanceForm1(request.POST, prefix='seance2')
                seance3 = SeanceForm1(request.POST, prefix='seance3')
                seance4 = SeanceForm1(request.POST , prefix='seance4')
                seance5 = SeanceForm1(request.POST , prefix='seance5')
                seance6 = SeanceForm1(request.POST , prefix='seance6')
                #---
                seance7 = SeanceForm1(request.POST ,prefix='seance7')
                seance8 = SeanceForm1(request.POST ,prefix='seance8')
                seance9 = SeanceForm1(request.POST ,prefix='seance9')
                seance10 = SeanceForm1(request.POST ,prefix='seance10')
                seance11 = SeanceForm1(request.POST ,prefix='seance11')
                seance12 = SeanceForm1(request.POST ,prefix='seance12')
            else:
                seance1 = SeanceForm1(request.POST, prefix='seance1' , instance=Seance.objects.filter(emploi=emplois , num_seance=1).first())
                seance2 = SeanceForm1(request.POST, prefix='seance2' , instance=Seance.objects.filter(emploi=emplois , num_seance=2).first())
                seance3 = SeanceForm1(request.POST, prefix='seance3' , instance=Seance.objects.filter(emploi=emplois , num_seance=3).first())
                seance4 = SeanceForm1(request.POST, prefix='seance4' , instance=Seance.objects.filter(emploi=emplois , num_seance=4).first())
                seance5 = SeanceForm1(request.POST, prefix='seance5' , instance=Seance.objects.filter(emploi=emplois , num_seance=5).first())
                seance6 = SeanceForm1(request.POST, prefix='seance6' , instance=Seance.objects.filter(emploi=emplois , num_seance=6).first())
                #---
                seance7 = SeanceForm1(request.POST,prefix='seance7' , instance=Seance.objects.filter(emploi=emplois , num_seance=7).first())
                seance8 = SeanceForm1(request.POST,prefix='seance8' , instance=Seance.objects.filter(emploi=emplois , num_seance=8).first())
                seance9 = SeanceForm1(request.POST,prefix='seance9' , instance=Seance.objects.filter(emploi=emplois, num_seance=9).first())
                seance10 = SeanceForm1(request.POST,prefix='seance10' , instance=Seance.objects.filter(emploi=emplois, num_seance=10).first())
                seance11 = SeanceForm1(request.POST,prefix='seance11' , instance=Seance.objects.filter(emploi=emplois, num_seance=11).first())
                seance12 = SeanceForm1(request.POST,prefix='seance12' , instance=Seance.objects.filter(emploi=emplois, num_seance=12).first())
            if seance1.is_valid() and seance2.is_valid() and seance3.is_valid() and seance4.is_valid() and seance5.is_valid() and seance6.is_valid()/\
                    seance7.is_valid() and seance8.is_valid() and seance9.is_valid() and seance10.is_valid() and seance11.is_valid() and seance12.is_valid():

                ####Seance 1 : Lundi
                seance1_1 = seance1.save(commit=False)
                seance1_1.date=emplois.dateDebut
                seance1_1.emploi = emplois
                seance1_1.num_seance = 1
                seance1_1.save()
                seance1.save_m2m()

                ###Seance 2 : Lundi
                seance2_1 = seance2.save(commit=False)
                seance2_1.date = emplois.dateDebut
                seance2_1.emploi = emplois
                seance2_1.num_seance = 2
                seance2_1.save()
                seance2.save_m2m()

                ###Seance 1 : Mardi
                seance3_1 = seance3.save(commit=False)
                seance3_1.date = emplois.dateDebut + datetime.timedelta(days=1)
                seance3_1.emploi = emplois
                seance3_1.num_seance = 3
                seance3_1.save()
                seance3.save_m2m()
                ###Seance 2 : Mardi
                seance4_1 = seance4.save(commit=False)
                seance4_1.date = emplois.dateDebut + datetime.timedelta(days=1)
                seance4_1.emploi = emplois
                seance4_1.num_seance = 4
                seance4_1.save()
                seance4.save_m2m()

                ###Seance 1 : Mercredi
                seance5_1 = seance5.save(commit=False)
                seance5_1.date = emplois.dateDebut + datetime.timedelta(days=2)
                seance5_1.emploi = emplois
                seance5_1.num_seance = 5
                seance5_1.save()
                seance5.save_m2m()

                ###Seance 2 : Mercredi
                seance6_1 = seance6.save(commit=False)
                seance6_1.date = emplois.dateDebut + datetime.timedelta(days=2)
                seance6_1.emploi = emplois
                seance6_1.num_seance = 6
                seance6_1.save()
                seance6.save_m2m()
                #----------------------

                ####Seance 1 : Jeudi
                seance7_1 = seance7.save(commit=False)
                seance7_1.date = emplois.dateDebut + datetime.timedelta(days=3)
                seance7_1.emploi = emplois
                seance7_1.num_seance = 7
                seance7_1.save()
                seance7.save_m2m()
                ###Seance 2 : Jeudi
                seance8_1 = seance8.save(commit=False)
                seance8_1.date = emplois.dateDebut + datetime.timedelta(days=3)
                seance8_1.emploi = emplois
                seance8_1.num_seance = 8
                seance8_1.save()
                seance8.save_m2m()


                ###Seance 1 : Vendredi
                seance9_1 = seance9.save(commit=False)
                seance9_1.date = emplois.dateDebut + datetime.timedelta(days=4)
                seance9_1.emploi = emplois
                seance9_1.num_seance = 9
                seance9_1.save()
                seance9.save_m2m()
                ###Seance 2 : Vendredi
                seance10_1 = seance10.save(commit=False)
                seance10_1.date = emplois.dateDebut + datetime.timedelta(days=4)
                seance10_1.emploi = emplois
                seance10_1.num_seance = 10
                seance10_1.save()
                seance10.save_m2m()

                ###Seance 1 : Samedi
                seance11_1 = seance11.save(commit=False)
                seance11_1.date = emplois.dateDebut + datetime.timedelta(days=5)
                seance11_1.emploi = emplois
                seance11_1.num_seance = 11
                seance11_1.save()
                seance11.save_m2m()

                ###Seance 2 : Samedi
                seance12_1 = seance12.save(commit=False)
                seance12_1.date = emplois.dateDebut + datetime.timedelta(days=5)
                seance12_1.emploi = emplois
                seance12_1.num_seance = 12
                seance12_1.save()
                seance12.save_m2m()
                promotion = Promotion.objects.filter(libelle=promotion).first()
                count_seance(promotion)
                emplois.observation = note
                emplois.save()
                if 'valider' in request.POST:
                    emplois.isValid = True
                    emplois.save()
                    return HttpResponseRedirect('/emploi_du_temps/')
                messages.success(request, 'Emploi du temps enregistrer avec succès')
            return render(request, 'Emploi/emploi_courant_add.html', locals())
        else:
            if seance:
                seance1 = SeanceForm1(prefix='seance1' , instance=Seance.objects.filter(emploi=emplois , num_seance=1).first())
                seance2 = SeanceForm1(prefix='seance2' , instance=Seance.objects.filter(emploi=emplois , num_seance=2).first())
                seance3 = SeanceForm1(prefix='seance3' , instance=Seance.objects.filter(emploi=emplois, num_seance=3).first())
                seance4 = SeanceForm1(prefix='seance4' , instance=Seance.objects.filter(emploi=emplois, num_seance=4).first())
                seance5 = SeanceForm1(prefix='seance5',instance=Seance.objects.filter(emploi=emplois, num_seance=5).first())
                seance6 = SeanceForm1(prefix='seance6',instance=Seance.objects.filter(emploi=emplois, num_seance=6).first())
                #----
                seance7 = SeanceForm1(prefix='seance7' , instance=Seance.objects.filter(emploi=emplois , num_seance=7).first())
                seance8 = SeanceForm1(prefix='seance8' , instance=Seance.objects.filter(emploi=emplois , num_seance=8).first())
                seance9 = SeanceForm1(prefix='seance9' , instance=Seance.objects.filter(emploi=emplois, num_seance=9).first())
                seance10 = SeanceForm1(prefix='seance10' , instance=Seance.objects.filter(emploi=emplois, num_seance=10).first())
                seance11 = SeanceForm1(prefix='seance11' , instance=Seance.objects.filter(emploi=emplois, num_seance=11).first())
                seance12 = SeanceForm1(prefix='seance12' , instance=Seance.objects.filter(emploi=emplois, num_seance=12).first())
                note = emplois.observation
            else:
                seance1 = SeanceForm1(prefix='seance1')
                seance2 = SeanceForm1(prefix='seance2')
                seance3 = SeanceForm1(prefix='seance3')
                seance4 = SeanceForm1(prefix='seance4')
                seance5 = SeanceForm1(prefix='seance5')
                seance6 = SeanceForm1(prefix='seance6')
                #--
                seance7 = SeanceForm1(prefix='seance7')
                seance8 = SeanceForm1(prefix='seance8')
                seance9 = SeanceForm1(prefix='seance9')
                seance10 = SeanceForm1(prefix='seance10')
                seance11 = SeanceForm1(prefix='seance11')
                seance12 = SeanceForm1(prefix='seance12')
            return render(request, 'Emploi/emploi_courant_add.html', locals())

    else:
        return render(request, 'Emploi/emploi_introuvable.html')

# les emploi des temps archivés:
def emploi_du_temps_archive_list(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    generate_emploi_archive()
    emploi = EmploiDuTemps.objects.filter(isValid=True)
    return render(request, 'Emploi/Emploi_du_temps_archive.html', {'emploi' : emploi})

def emploi_du_temps_archive(request , semestre , semaine , promotion):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    semestres = Semestre.objects.filter(libelle=semestre, promotion__libelle=promotion).first()
    emplois = EmploiDuTemps.objects.filter(semestre=semestres, semaine__num_semaine=semaine , isValid=True).first()
    note = emplois.observation
    if semestres and emplois:
        seance1 = Seance.objects.filter(emploi=emplois, num_seance=1).first()
        seance2 = Seance.objects.filter(emploi=emplois, num_seance=2).first()
        seance3 = Seance.objects.filter(emploi=emplois, num_seance=3).first()
        seance4 = Seance.objects.filter(emploi=emplois, num_seance=4).first()
        seance5 = Seance.objects.filter(emploi=emplois, num_seance=5).first()
        seance6 = Seance.objects.filter(emploi=emplois, num_seance=6).first()
        seance7 = Seance.objects.filter(emploi=emplois, num_seance=7).first()
        seance8 = Seance.objects.filter(emploi=emplois, num_seance=8).first()
        seance9 = Seance.objects.filter(emploi=emplois, num_seance=9).first()
        seance10 = Seance.objects.filter(emploi=emplois, num_seance=10).first()
        seance11 = Seance.objects.filter(emploi=emplois, num_seance=11).first()
        seance12 = Seance.objects.filter(emploi=emplois, num_seance=12).first()
        return render(request, 'Emploi/emploi_grave.html', locals())
    else:
        return render(request, 'Emploi/emploi_introuvable.html')

def imprimer(request):
    emplois = request.POST['emploi']
    emploi = EmploiDuTemps.objects.get(id=emplois)
    seance1 = Seance.objects.filter(emploi__id=emplois, num_seance=1).first()
    seance2 = Seance.objects.filter(emploi__id=emplois, num_seance=2).first()
    seance3 = Seance.objects.filter(emploi__id=emplois, num_seance=3).first()
    seance4 = Seance.objects.filter(emploi__id=emplois, num_seance=4).first()
    seance5 = Seance.objects.filter(emploi__id=emplois, num_seance=5).first()
    seance6 = Seance.objects.filter(emploi__id=emplois, num_seance=6).first()
    seance7 = Seance.objects.filter(emploi__id=emplois, num_seance=7).first()
    seance8 = Seance.objects.filter(emploi__id=emplois, num_seance=8).first()
    seance9 = Seance.objects.filter(emploi__id=emplois, num_seance=9).first()
    seance10 = Seance.objects.filter(emploi__id=emplois, num_seance=10).first()
    seance11 = Seance.objects.filter(emploi__id=emplois, num_seance=11).first()
    seance12 = Seance.objects.filter(emploi__id=emplois, num_seance=12).first()
    semestre = emploi.semestre
    if semestre.libelle.upper() == "S1" or semestre.libelle.upper() == "S2":
        level =  "1ERE ANNÉE " + str(semestre.libelle)
    elif semestre.libelle.upper() == "S3" or semestre.libelle.upper() == "S4":
        level = "2EME ANNÉE " + str(semestre.libelle)
    else:
        level = "3EME ANNÉE " + str(semestre.libelle)
    template = get_template('pdf_candidat.html')
    html  = template.render(locals())
    file = open('pdf.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
            encoding='utf-8')
    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, 'application/pdf')

def no(request , id, month , year):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    prof = Professeur.objects.filter(id=id).first()
    count_sema = 1
    month = int(month)
    year = int(year)
    fin = last_day_of_month(datetime.date(year,month, 1))
    debut = datetime.date(year,month,1)
    charge = Horaire_semaine.objects.filter(professeur=prof , dateDebut__gte=debut , dateFin__lte=fin ).first()
    seance = Seance.objects.distinct().filter(Q(date__gte=debut) & Q(date__lte=fin) & (
    Q(professeur_firstgroup=Professeur.objects.filter(id=id).first()) | Q(
        professeur_secondgroup=Professeur.objects.filter(id=id).first()))).first()


    semaine1 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine1").first())
    semaine2 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine2").first())
    semaine3 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine3").first())
    semaine4 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine4").first())
    semaine5 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine5").first())

    count_horaire = Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin).aggregate(total=Sum('Charge_realise'))
    taux_brut = prof.diplome.taux_brut
    taux_net = prof.diplome.taux_net
    count_net =  count_horaire['total']* taux_brut
    count_brut = count_horaire['total'] * taux_net
    words = num2words(count_net, lang='fr') + " Dirhams"
    return render(request, 'memoire.html' , locals())




def fiche(request , id, month , year):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    prof = Professeur.objects.filter(id=id).first()
    count_sema = 1
    month = int(month)
    year = int(year)
    fin = last_day_of_month(datetime.date(year,month, 1))
    debut = datetime.date(year,month,1)
    charge = Horaire_semaine.objects.filter(professeur=prof , dateDebut__gte=debut , dateFin__lte=fin ).first()
    seance = Seance.objects.distinct().filter(Q(date__gte=debut) & Q(date__lte=fin) & (
    Q(professeur_firstgroup=Professeur.objects.filter(id=id).first()) | Q(
        professeur_secondgroup=Professeur.objects.filter(id=id).first()))).first()


    semaine1 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine1").first())
    semaine2 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine2").first())
    semaine3 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine3").first())
    semaine4 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine4").first())
    semaine5 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine5").first())

    count_horaire = Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin).aggregate(total=Sum('Charge_realise'))
    if prof.type == "Vacataire" and prof.diplome:
        taux_brut = prof.diplome.taux_brut
        taux_net = prof.diplome.taux_net
        count_net =  count_horaire['total']* taux_brut
        count_brut = count_horaire['total'] * taux_net
        words = num2words(count_net, lang='fr') + " Dirhams"

    template = get_template('memoire.html')
    html  = template.render(locals())
    file = open('pdf.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
            encoding='utf-8')
    file.seek(0)
    pdf = file.read()
    file.close()

    return HttpResponse(pdf, 'application/pdf')
def facturation(request , id , month , year , matiere):

    #check authentification
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    #
    prof = Professeur.objects.filter(id=id).first()
    matiere = Matiere.objects.filter(id = matiere).first()
    month = int(month)
    year = int(year)
    fin = last_day_of_month(datetime.date(year,month, 1))
    debut = datetime.date(year,month,1)
    charge = Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin)
    chargse = Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin).count()
    count_horaire = 0
    for i in charge:
        seance = Seance.objects.filter(Q(date__gte=i.dateDebut) & Q(date__lte=i.dateFin) &Q(matiere=matiere) &(
        Q(professeur_firstgroup=prof) | Q(professeur_secondgroup=prof)))

        hora = Horaire_jour.objects.filter(horaire_semaine=i , professeur = prof , matiere= matiere).first()
        if hora :
            hora.delete()

        horaire_jour = Horaire_jour(horaire_semaine=i, professeur=prof , matiere = matiere)
        for i in seance:
            if i.num_seance == 1:
                horaire_jour.lundi = "03H30"
                count_horaire+=1
            elif i.num_seance == 2:
                if horaire_jour.lundi == None:
                    horaire_jour.lundi = "03H30"
                    count_horaire += 1
                else:
                    horaire_jour.lundi = "07H"
                    count_horaire += 1

            if i.num_seance == 3:
                horaire_jour.Mardi = "03H30"
                count_horaire += 1

            elif i.num_seance == 4:
                if horaire_jour.Mardi == None:
                    horaire_jour.Mardi = "03H30"
                    count_horaire += 1
                else:
                    horaire_jour.Mardi = "07H"
                    count_horaire += 1

            if i.num_seance == 5:
                horaire_jour.Mercredi = "03H30"
                count_horaire += 1
            elif i.num_seance == 6:
                if horaire_jour.Mercredi == None:
                    horaire_jour.Mercredi = "03H30"
                    count_horaire += 1
                else:
                    horaire_jour.Mercredi = "07H"
                    count_horaire += 1

            if i.num_seance == 7:
                horaire_jour.Jeudi = "03H30"
                count_horaire += 1
            elif i.num_seance == 8:
                if horaire_jour.Jeudi == None:
                    horaire_jour.Jeudi = "03H30"
                    count_horaire += 1
                else:
                    horaire_jour.Jeudi = "07H"
                    count_horaire += 1

            if i.num_seance == 9:
                horaire_jour.Vendredi = "03H30"
                count_horaire += 1
            elif i.num_seance == 10:
                if horaire_jour.Vendredi == None:
                    horaire_jour.Vendredi = "03H30"
                    count_horaire += 1
                else:
                    horaire_jour.Vendredi = "07H"
                    count_horaire += 1

            if i.num_seance == 11:
                horaire_jour.Samedi = "03H30"
                count_horaire += 1
            elif i.num_seance == 12:
                if horaire_jour.Samedi == None:
                    horaire_jour.Samedi = "03H30"
                    count_horaire += 1
                else:
                    horaire_jour.Samedi = "07H"
                    count_horaire += 1
            horaire_jour.total = count_horaire*3.5
            horaire_jour.save()

    semaine1 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine1").first() , professeur=prof  , matiere=matiere)
    semaine2 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter( dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine2").first() , professeur=prof , matiere=matiere)
    semaine3 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine3").first() , professeur=prof , matiere=matiere)
    semaine4 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine4").first() , professeur=prof , matiere=matiere)
    semaine5 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine5").first() , professeur=prof , matiere=matiere)
    count_horaire = count_horaire*3.5
    dec = count_horaire % 1
    sim = count_horaire // 1

    if prof.type == "Vacataire" and prof.diplome:
        taux_brut = prof.diplome.taux_brut
        taux_net = prof.diplome.taux_net
        count_net =  Decimal(count_horaire) * Decimal(taux_brut)
        count_brut = Decimal(count_horaire) * Decimal(taux_net)
        words = num2words(count_net, lang='fr') + " Dirhams"
    return render(request, 'facture.html', locals())
def facturation_modif(request , id , month , year , matiere):

    #check authentification
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    #
    prof = Professeur.objects.filter(id=id).first()
    matiere = Matiere.objects.filter(id = matiere).first()
    month = int(month)
    year = int(year)
    fin = last_day_of_month(datetime.date(year,month, 1))
    debut = datetime.date(year,month,1)
    charge = Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin)
    count_horaire = 0
    for i in charge:
        hora = Horaire_jour.objects.filter(horaire_semaine=i , professeur = prof , matiere = matiere).first()
        if hora :
            count_horaire = hora.total_modif
    semaine1 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine1").first() , professeur=prof  , matiere=matiere)
    semaine2 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter( dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine2").first() , professeur=prof , matiere=matiere)
    semaine3 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine3").first() , professeur=prof , matiere=matiere)
    semaine4 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine4").first() , professeur=prof , matiere=matiere)
    semaine5 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine5").first() , professeur=prof , matiere=matiere)

    dec = count_horaire % 1
    sim = count_horaire // 1


    if prof.type == "Vacataire" and prof.diplome:
        taux_brut = prof.diplome.taux_brut
        taux_net = prof.diplome.taux_net
        count_net =  Decimal(count_horaire) * Decimal(taux_brut)
        count_brut = Decimal(count_horaire) * Decimal(taux_net)
        words = num2words(count_net, lang='fr') + " Dirhams"
    return render(request, 'facture_modif.html', locals())
def facturation_modif_memoire(request , id , month , year , matiere):

    #check authentification
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
        #
    prof = Professeur.objects.filter(id=id).first()
    matiere = Matiere.objects.filter(id = matiere).first()
    month = int(month)
    year = int(year)
    fin = last_day_of_month(datetime.date(year,month, 1))
    debut = datetime.date(year,month,1)
    charge = Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin)
    count_horaire = 0
    for i in charge:
        hora = Horaire_jour.objects.filter(horaire_semaine=i , professeur = prof , matiere = matiere).first()
        if hora :
            count_horaire = hora.total_modif
    semaine1 = Horaire_jour.objects.filter(
            horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                           libelle="Semaine1").first() , professeur=prof  , matiere=matiere)
    semaine2 = Horaire_jour.objects.filter(
            horaire_semaine=Horaire_semaine.objects.filter( dateDebut__gte=debut, dateFin__lte=fin,
                                                           libelle="Semaine2").first() , professeur=prof , matiere=matiere)
    semaine3 = Horaire_jour.objects.filter(
            horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                           libelle="Semaine3").first() , professeur=prof , matiere=matiere)
    semaine4 = Horaire_jour.objects.filter(
            horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                           libelle="Semaine4").first() , professeur=prof , matiere=matiere)
    semaine5 = Horaire_jour.objects.filter(
            horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                           libelle="Semaine5").first() , professeur=prof , matiere=matiere)

    dec = count_horaire % 1
    sim = count_horaire // 1


    if prof.type == "Vacataire" and prof.diplome:
        taux_brut = prof.diplome.taux_brut
        taux_net = prof.diplome.taux_net
        count_net =  Decimal(count_horaire) * Decimal(taux_brut)
        count_brut = Decimal(count_horaire) * Decimal(taux_net)
        words = num2words(count_net, lang='fr') + " Dirhams"

    return render(request, 'modification_facture.html', locals())
def fiche_modif(request , id , month , year , matiere):

    #check authentification
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    #
    prof = Professeur.objects.filter(id=id).first()
    matiere = Matiere.objects.filter(id = matiere).first()
    month = int(month)
    year = int(year)
    fin = last_day_of_month(datetime.date(year,month, 1))
    debut = datetime.date(year,month,1)
    charge = Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin)
    count_horaire = 0
    for i in charge:
        hora = Horaire_jour.objects.filter(horaire_semaine=i , professeur = prof , matiere = matiere).first()
        if hora :
            count_horaire = hora.total_modif
    semaine1 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine1").first() , professeur=prof  , matiere=matiere)
    semaine2 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter( dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine2").first() , professeur=prof , matiere=matiere)
    semaine3 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine3").first() , professeur=prof , matiere=matiere)
    semaine4 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine4").first() , professeur=prof , matiere=matiere)
    semaine5 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine5").first() , professeur=prof , matiere=matiere)

    dec = count_horaire % 1
    sim = count_horaire // 1


    if prof.type == "Vacataire" and prof.diplome:
        taux_brut = prof.diplome.taux_brut
        taux_net = prof.diplome.taux_net
        count_net =  Decimal(count_horaire) * Decimal(taux_brut)
        count_brut = Decimal(count_horaire) * Decimal(taux_net)
        words = num2words(count_net, lang='fr') + " Dirhams"
    template = get_template('memoire_modif.html')
    html = template.render(locals())
    file = open('pdf.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
                                encoding='utf-8')
    file.seek(0)
    pdf = file.read()
    file.close()

    return HttpResponse(pdf, 'application/pdf')
@csrf_exempt
def facturation_modif_done(request , id , month , year , matiere):
    prof = Professeur.objects.filter(id=id).first()
    matiere = Matiere.objects.filter(id = matiere).first()
    if request.method == "POST":
        total = request.POST['total']
        semaine1_lundi = request.POST['semaine1_lundi']
        semaine2_lundi = request.POST['semaine2_lundi']
        semaine3_lundi = request.POST['semaine3_lundi']
        semaine4_lundi = request.POST['semaine4_lundi']
        semaine5_lundi = request.POST['semaine5_lundi']
        semaine1_mardi = request.POST['semaine1_mardi']
        semaine2_mardi = request.POST['semaine2_mardi']
        semaine3_mardi = request.POST['semaine3_mardi']
        semaine4_mardi = request.POST['semaine4_mardi']
        semaine5_mardi = request.POST['semaine5_mardi']
        semaine1_mercredi = request.POST['semaine1_mercredi']
        semaine2_mercredi = request.POST['semaine2_mercredi']
        semaine3_mercredi = request.POST['semaine3_mercredi']
        semaine4_mercredi = request.POST['semaine4_mercredi']
        semaine5_mercredi = request.POST['semaine5_mercredi']
        semaine1_jeudi = request.POST['semaine1_jeudi']
        semaine2_jeudi = request.POST['semaine2_jeudi']
        semaine3_jeudi = request.POST['semaine3_jeudi']
        semaine4_jeudi = request.POST['semaine4_jeudi']
        semaine5_jeudi = request.POST['semaine5_jeudi']
        semaine1_vendredi = request.POST['semaine1_vendredi']
        semaine2_vendredi = request.POST['semaine2_vendredi']
        semaine3_vendredi = request.POST['semaine3_vendredi']
        semaine4_vendredi = request.POST['semaine4_vendredi']
        semaine5_vendredi = request.POST['semaine5_vendredi']
        semaine1_samedi = request.POST['semaine1_samedi']
        semaine2_samedi = request.POST['semaine2_samedi']
        semaine3_samedi = request.POST['semaine3_samedi']
        semaine4_samedi = request.POST['semaine4_samedi']
        semaine5_samedi = request.POST['semaine5_samedi']
        month = int(month)
        year = int(year)
        fin = last_day_of_month(datetime.date(year, month, 1))
        debut = datetime.date(year, month, 1)
        charge = Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin)
        for i in charge:
            hora = Horaire_jour.objects.filter(horaire_semaine=i, professeur=prof, matiere=matiere).first()
            if not hora:
                hora = Horaire_jour(horaire_semaine=i, professeur=prof, matiere=matiere)
            if i.libelle == 'Semaine1':
                hora.lundi_modif = semaine1_lundi
                hora.Mardi_modif = semaine1_mardi
                hora.Mercredi_modif = semaine1_mercredi
                hora.Jeudi_modif = semaine1_jeudi
                hora.Vendredi_modif = semaine1_vendredi
                hora.Samedi_modif = semaine1_samedi
                hora.total_modif = total
                hora.save()
            elif i.libelle == "Semaine2":
                hora.lundi_modif = semaine2_lundi
                hora.Mardi_modif = semaine2_mardi
                hora.Mercredi_modif = semaine2_mercredi
                hora.Jeudi_modif = semaine2_jeudi
                hora.Vendredi_modif = semaine2_vendredi
                hora.Samedi_modif = semaine2_samedi
                hora.total_modif = total
                hora.save()
            elif i.libelle == "Semaine3":
                hora.lundi_modif = semaine3_lundi
                hora.Mardi_modif = semaine3_mardi
                hora.Mercredi_modif = semaine3_mercredi
                hora.Jeudi_modif = semaine3_jeudi
                hora.Vendredi_modif = semaine3_vendredi
                hora.Samedi_modif = semaine3_samedi
                hora.total_modif = total
                hora.save()
            elif i.libelle == "Semaine4":
                hora.lundi_modif = semaine4_lundi
                hora.Mardi_modif = semaine4_mardi
                hora.Mercredi_modif = semaine4_mercredi
                hora.Jeudi_modif = semaine4_jeudi
                hora.Vendredi_modif = semaine4_vendredi
                hora.Samedi_modif = semaine4_samedi
                hora.total_modif = total
                hora.save()
            elif i.libelle == "Semaine5":
                hora.lundi_modif = semaine5_lundi
                hora.Mardi_modif = semaine5_mardi
                hora.Mercredi_modif = semaine5_mercredi
                hora.Jeudi_modif = semaine5_jeudi
                hora.Vendredi_modif = semaine5_vendredi
                hora.Samedi_modif = semaine5_samedi
                hora.total_modif = total
                hora.save()
        path =  re.sub('/modif/done$', '/', request.path)
        print(path)
        return HttpResponseRedirect(path)
    else:
        return render(request, 'index.html')
def fichee(request , id , month , year , matiere):

    #check authentification
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    #
    prof = Professeur.objects.filter(id=id).first()
    matiere = Matiere.objects.filter(id = matiere).first()
    month = int(month)
    year = int(year)
    fin = last_day_of_month(datetime.date(year,month, 1))
    debut = datetime.date(year,month,1)
    charge = Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin)
    count_horaire = 0
    for i in charge:
        hora = Horaire_jour.objects.filter(horaire_semaine=i , professeur = prof , matiere = matiere).first()
        if hora :
            if count_horaire < hora.total:
                count_horaire = hora.total

    semaine1 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine1").first() , professeur=prof  , matiere=matiere)
    semaine2 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter( dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine2").first() , professeur=prof , matiere=matiere)
    semaine3 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine3").first() , professeur=prof , matiere=matiere)
    semaine4 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine4").first() , professeur=prof , matiere=matiere)
    semaine5 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine5").first() , professeur=prof , matiere=matiere)


    dec = count_horaire % 1
    sim = count_horaire // 1


    if prof.type == "Vacataire" and prof.diplome:
        taux_brut = prof.diplome.taux_brut
        taux_net = prof.diplome.taux_net
        count_net =  Decimal(count_horaire) * Decimal(taux_brut)
        count_brut = Decimal(count_horaire) * Decimal(taux_net)
        words = num2words(count_net, lang='fr') + " Dirhams"

    template = get_template('memoire.html')
    html = template.render(locals())
    file = open('pdf.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
                                encoding='utf-8')
    file.seek(0)
    pdf = file.read()
    file.close()

    return HttpResponse(pdf, 'application/pdf')

def gestion_etudiant(request , promotion):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    etudiant = Etudiant.objects.filter(promotion__libelle=promotion)
    promotion = promotion
    return render(request,'gestion_etudiant.html',locals())

def prof(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    year_begin = str(datetime.date.today().year -1)
    year_fin = str(datetime.date.today().year)
    prof = Professeur.objects.filter(matiere__semestre__annee_universitaire=str(year_begin+ "/"+year_fin)).distinct()
    return render(request,'prof.html',locals())

def moiss(request, id):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    year_begin = str(datetime.date.today().year -1)
    year_fin = str(datetime.date.today().year)
    month = datetime.date.today().month
    list_month = []

    if month <9:
        mt = 9
        while(mt != month):
            list_month.append(mt)
            mt+=1
            if mt == 13:
                mt=1
    else:
        mt=9
        while (mt != month):
            list_month.append(mt)
            mt+=1
    list_month.append(month)
    list_month = list_month
    print(list_month)
    return render(request, 'prof_mois.html' , locals())

def mois(request, id):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')

    date_seance = Seance.objects.filter(Q(professeur_firstgroup=id) or Q(professeur_secondgroup=id)).values('date').distinct()
    print(date_seance)
    list_month = []

    for i in date_seance:
       mo = set_mois(i['date'].month , i['date'].year)
       if list_month:
           exist = 0
           for a in list_month:

               if mo.mois == a.mois and mo.year == a.year:
                   exist = 1
           if exist == 0:
                list_month.append(mo)
       else:
           list_month.append(mo)
    return render(request, 'prof_mois.html' , locals())

def promotion_list(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    promo = Promotion.objects.all()

    return render(request,'promo_list.html' ,locals())

def semestre_list(request , promotion):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    semestre = Semestre.objects.filter(promotion__libelle = promotion)
    return render(request, 'semestre_list.html', locals())

def matiere(request , promotion , semestre):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    matiere = Matiere.objects.filter(semestre__libelle=semestre).order_by('semestre')
    return render(request, 'matiere/matiere.html', locals())

class set_matiere_prof(object):
    def __init__(self, matiere, prof):
        self.matiere = matiere
        self.prof = prof

def fiche_matiere(request , promotion , semestre):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    list_prof = []
    list_matiere_prof = []
    matiere = Matiere.objects.filter(semestre__libelle=semestre).order_by('semestre')
    print(matiere)
    for i in matiere:
        Prof = Professeur.objects.filter(matiere = i)
        for a in Prof:
            list_prof.append(a)
        c = set_matiere_prof(i , list_prof)
        list_matiere_prof.append(c)
        list_prof = []

    template = get_template('etats_matiere_pdf.html')
    html = template.render(locals())
    file = open('pdf.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
                                encoding='utf-8')
    file.seek(0)
    pdf = file.read()
    file.close()

    return HttpResponse(pdf, 'application/pdf')

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

def kokos(request , id , month , year):
    #check authentification
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    #

    prof = Professeur.objects.filter(id=id).first()
    count_sema = 1
    month = int(month)
    year = int(year)
    fin = last_day_of_month(datetime.date(year,month, 1))
    debut = datetime.date(year,month,1)
    charge = Horaire_semaine.objects.filter(professeur=prof , dateDebut__gte=debut , dateFin__lte=fin ).first()
    seance = Seance.objects.distinct().filter(Q(date__gte=debut) & Q(date__lte=fin) & (
    Q(professeur_firstgroup=Professeur.objects.filter(id=id).first()) | Q(
        professeur_secondgroup=Professeur.objects.filter(id=id).first()))).first()

    if not charge:
        #nom du mois:
        #month_name = datetime.date.today().strftime('%B')
        #debut et fin

        yo= debut
        seance_count = Seance.objects.filter(date__gte=yo , date__lte=fin).count()
        #generation des semaines du mois :
        start_of_week = yo
        while yo <= fin:
            weekday = yo.weekday()
            start_delta = datetime.timedelta(days=weekday)
            start_of_week = yo - start_delta
            final = fin
            if start_of_week + datetime.timedelta(days=7) > fin:
                week_dates = [start_of_week]
                i=1
                while(i<7):
                    if(start_of_week + datetime.timedelta(days=i) <= fin):
                        final = start_of_week + datetime.timedelta(days=i)
                        week_dates.append(start_of_week + datetime.timedelta(days=i))
                        i+=1
                    else:
                        yo = fin+datetime.timedelta(days=1)
                        break;
            else:
                if start_of_week < yo :
                    start_of_week = yo
                    week_dates = [yo + datetime.timedelta(days=i) for i in range(7-yo.weekday())]
                    yo = week_dates[-1] + datetime.timedelta(days=1)
                else:
                    week_dates = [start_of_week + datetime.timedelta(days=i) for i in range(7)]
                    yo = week_dates[6] + datetime.timedelta(days=1)


            semaine = "Semaine" + str(count_sema)
            seance = Seance.objects.distinct().filter(Q(date__gte=week_dates[0]) & Q(date__lte=week_dates[-1]) & (Q(professeur_firstgroup=Professeur.objects.filter(id=id).first()) | Q(professeur_secondgroup=Professeur.objects.filter(id=id).first()))).count()
            Horaire = Horaire_semaine(libelle=semaine, dateDebut=week_dates[0], dateFin=week_dates[-1], professeur=prof , Charge_realise = seance*3.5)
            Horaire.save()
            seance_facture = Seance.objects.distinct().filter(Q(date__gte=week_dates[0]) & Q(date__lte=week_dates[-1]) & (Q(professeur_firstgroup=Professeur.objects.filter(id=id).first()) | Q(professeur_secondgroup=Professeur.objects.filter(id=id).first())))
            horaire_jour = Horaire_jour(horaire_semaine=Horaire)
            for i in seance_facture:
                if i.num_seance == 1:
                    horaire_jour.lundi = "3H30"
                elif i.num_seance == 2:
                    if horaire_jour.lundi == None:
                        horaire_jour.lundi = "3H30"
                    else:
                        horaire_jour.lundi = "7H"

                if i.num_seance == 3:
                    horaire_jour.Mardi = "3H30"

                elif i.num_seance == 4:
                    if horaire_jour.Mardi == None :
                        horaire_jour.Mardi = "3H30"
                    else:
                        horaire_jour.Mardi = "7H"

                if i.num_seance == 5:
                    horaire_jour.Mercredi = "3H30"
                elif i.num_seance == 6:
                    if horaire_jour.Mercredi == None:
                        horaire_jour.Mercredi = "3H30"
                    else:
                        horaire_jour.Mercredi = "7H"

                if i.num_seance == 7:
                    horaire_jour.Jeudi = "3H30"
                elif i.num_seance == 8:
                    if horaire_jour.Jeudi == None:
                        horaire_jour.Jeudi = "3H30"
                    else:
                        horaire_jour.Jeudi = "7H"

                if i.num_seance == 9:
                    horaire_jour.Vendredi = "3H30"
                elif i.num_seance == 10:
                    if horaire_jour.Vendredi == None:
                        horaire_jour.Vendredi = "3H30"
                    else:
                        horaire_jour.Vendredi = "7H"

                if i.num_seance == 11:
                    horaire_jour.Samedi = "3H30"
                elif i.num_seance == 12:
                    if horaire_jour.Samedi == None:
                        horaire_jour.Samedi = "3H30"
                    else:
                        horaire_jour.Samedi = "7H"

                horaire_jour.save()
            count_sema+=1


    semaine1 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine1").first())
    semaine2 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine2").first())
    semaine3 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine3").first())
    semaine4 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine4").first())
    semaine5 = Horaire_jour.objects.filter(
        horaire_semaine=Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin,
                                                       libelle="Semaine5").first())
    count_horaire = Horaire_semaine.objects.filter(professeur=prof, dateDebut__gte=debut, dateFin__lte=fin).aggregate(
        total=Sum('Charge_realise'))

    if prof.type == "Vacataire" and prof.diplome:
        taux_brut = prof.diplome.taux_brut
        taux_net = prof.diplome.taux_net
        count_net =  count_horaire['total']* taux_brut
        count_brut = count_horaire['total'] * taux_net
        words = num2words(count_net, lang='fr') + " Dirhams"
    return render(request, 'facture.html' , locals())

def facture(request , id , month , year):
    #check authentification
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    #
    count_sema = 1
    prof = Professeur.objects.filter(id=id).first()
    month = int(month)
    year = int(year)
    fin = last_day_of_month(datetime.date(year,month, 1))
    debut = datetime.date(year,month,1)

    charge = Horaire_semaine.objects.filter(dateDebut__gte=debut, dateFin__lte=fin).first()

    if not charge :
        yo= debut
        #generation des semaines du mois :
        start_of_week = yo
        while yo < fin:
            weekday = yo.weekday()
            start_delta = datetime.timedelta(days=weekday)
            start_of_week = yo - start_delta
            final = fin

            if start_of_week + datetime.timedelta(days=7) > fin:
                week_dates = [start_of_week]
                i=1
                while(i<7):
                    if(start_of_week + datetime.timedelta(days=i) <= fin):
                        final = start_of_week + datetime.timedelta(days=i)
                        week_dates.append(start_of_week + datetime.timedelta(days=i))
                        i+=1
                        yo = week_dates[-1]
                    else:
                        yo = fin+datetime.timedelta(days=1)
                        break;
            else:
                if start_of_week < yo :
                    start_of_week = yo
                    week_dates = [yo + datetime.timedelta(days=i) for i in range(7-yo.weekday())]
                    yo = week_dates[-1] + datetime.timedelta(days=1)
                else:
                    week_dates = [start_of_week + datetime.timedelta(days=i) for i in range(7)]
                    yo = week_dates[6] + datetime.timedelta(days=1)
            semaine = "Semaine" + str(count_sema)
            seance = Seance.objects.distinct().filter(Q(date__gte=week_dates[0]) & Q(date__lte=week_dates[-1]) & (Q(professeur_firstgroup=Professeur.objects.filter(id=id).first()) | Q(professeur_secondgroup=Professeur.objects.filter(id=id).first()))).count()
            Horaire = Horaire_semaine(libelle=semaine, dateDebut=week_dates[0], dateFin=week_dates[-1])
            Horaire.save()
            count_sema +=1
    matiere = Matiere.objects.filter(professeur=prof)
    print(matiere)
    return render(request , 'matiere_by_teacher.html' , locals())


#lié au repértoire téléphonique
def repertoire_prof(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    prof = Professeur.objects.all()
    return render(request, 'prof_repertoire.html' ,locals())

#Repertoire des étudiants
def repertoire_etud(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    etudiant = Etudiant.objects.all()
    return render(request, 'etudiant_repertoire.html' ,locals())


#utilisé dans Ajax
def getProf(request):
    id = request.POST['id']
    professeur = Professeur.objects.filter(matiere__id=id)
    optionsHtml = ""
    for prof in professeur:
        optionsHtml+="<option value='{0}'>{1}</option>".format(prof.id,prof.nom)
    return HttpResponse(optionsHtml)
def getVide(request):
    optionsHtml = ""
    return HttpResponse(optionsHtml)
def getSeance(request):
    i=0
    id = request.POST['id']
    token = request.POST['token']
    laps = request.POST.getlist('laps[]')
    for a in laps:
        if id == a:
            i+=1
    matiere = Matiere.objects.get(id=id)
    if (matiere.seanceRealise +1) > (matiere.chargeHoraire/3.5):
        a= "<input style='background-color : rgba(255, 0, 0, 0.2);' type='text' name='"+ token + "' maxlength='20' id='id_" + token + "' value=' Seance " + str(matiere.seanceRealise + i) + "' >"
    else:
        a= "<input type='text' name='"+ token + "' maxlength='20' id='id_" + token + "' value=' Seance " + str(matiere.seanceRealise + i) + "' >"


    return HttpResponse(a)
def getSeance1(request):
    matiere = Matiere.objects.get(id=id)
    a = "Seance "+ str(matiere.seanceRealise + 1)
    return HttpResponse(a)
def getMatiere(request):

    pr = request.POST['pr']
    selected = request.POST['selected_value']
    print(selected)
    b=""

    pr = Promotion.objects.get(libelle=pr)
    matiere = Matiere.objects.filter(semestre__promotion=pr).order_by("semestre")
    optionsHtml = "<option value=''>-LIBRE-</option>"
    for a in matiere:
        if b != a.semestre.libelle:
            b=a.semestre.libelle
            optionsHtml+="<option value='' style='background:#eee'>-----------------------------------------{0}-----------------------------------------</option>".format(b)

        if selected and a.id == int(selected):
            optionsHtml+="<option value='{0}' selected>{1}</option>".format(a.id,a.libelle)
        else:
            optionsHtml += "<option value='{0}' >{1}</option>".format(a.id, a.libelle)
    return HttpResponse(optionsHtml)
def generate_PDF(request,cin , promotion):
    etudiant= Etudiant.objects.get(cin=cin)
    tag = str(etudiant.image)
    tag = "../"+tag
    print(tag.replace('app' , '..'))
    template = get_template('pdf_fiche.html')
    html  = template.render(locals())
    file = open('pdf.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
            encoding='utf-8')
    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, 'application/pdf')



def fiche_renseignement(request,cin , promotion):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
    etudiant = Etudiant.objects.filter(cin=cin).first()
    return render(request,'fiche_renseignement.html', locals())

def accueil(request):
    user = request.user
    if user.is_authenticated:
        if user.is_verrou == True:
            return HttpResponseRedirect('/verouille')
        return render(request, 'index.html')

    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User = authenticate(username = username , password = password)
            login(request, User)
            return HttpResponseRedirect('/accueil')

    return render(request, 'accueil.html' , locals())

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
def check_login(request):
    check_authentification()
    if request.method=="POST":
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(password)
        User = authenticate(username=username, password=password)
        if User:
            login(request, User)
            User.is_verrou = False
            User.save()
            return HttpResponse("<meta http-equiv='Refresh' content=\"0;url=http://127.0.0.1:8000/accueil/ \"> ")

        else:
            return HttpResponse("<div class='alert alert-danger'><b>Erreur!</b> le mot de passe est incorrect</div>")
    else:
        return HttpResponse('hooo')

def verrou(request):
    user = request.user
    if not user.is_authenticated:
        print("walo")
        return HttpResponseRedirect("/")
    else:
        if user.is_verrou == True:
            print('daz true a sat')
        else:
            user.is_verrou = True
            user.save()
    return render(request,'lock_page.html')


#views for accueil
def index_event(request):
    return render(request, 'event.html')
def event(request):
    json_list = []
    event = Events.objects.all()
    for i in event:
        id = i.id
        title = i.title
        start = i.start.strftime("%Y-%m-%dT%H:%M:%S")
        end = i.end.strftime("%Y-%m-%dT%H:%M:%S")
        color = i.color
        json_event = {'id':id,'title':title , 'start':start, 'end':end, 'color': color}
        json_list.append(json_event)
    return HttpResponse(json.dumps(json_list), content_type='application/json')
def edit(request):
    if request.method == "POST":
        Event = request.POST.getlist('laps[]')
        id = Event[0]
        start = Event[1]
        end = Event[2]
        event = Events.objects.filter(id = id).first()
        event.start = start
        event.end = end
        event.save()
@csrf_exempt
def edit_info(request):
    id = request.POST['id']
    delete= request.POST.get('delete', False);
    if id and delete :
        e = Events.objects.filter(id = id ).first()
        e.delete()
    else:
        title = request.POST['title']
        color = request.POST['color']
        e = Events.objects.filter(id = id ).first()
        e.title = title
        e.color = color
        e.save()
    return HttpResponseRedirect('/accueil')
def addEvent(request):

    title = request.POST['title']
    start = request.POST['start']
    end = request.POST['end'];
    color = request.POST['color'];
    if title and start and end and color:
        e = Events(title = title , start = start , end= end , color = color)
        e.save()
    return HttpResponseRedirect('/accueil')
def tuto(request):
    return render(request , 'tuto.html')
class annee_and_charge(object):
    def __init__(self, annee, charge):
        self.annee = annee
        self.charge = charge
def annee(request , id):
    datedebut = datetime.date(1996,10,10)
    datefin = datetime.date(1996,10,10)
    counter = 0
    annees = Semestre.objects.all().values('annee_universitaire').distinct()
    list = []
    for a in annees:
        sem = Semestre.objects.filter(annee_universitaire=a['annee_universitaire'])
        for k in sem:
            if counter == 0:
                datedebut = k.dateDebut
                counter+=1
            if datedebut > k.dateDebut:
                datedebut = k.dateDebut
            if datefin< k.dateFin:
                datefin = k.dateFin
        prof = Professeur.objects.filter(id=id).first()
        seance = Seance.objects.filter(Q(date__gte=datedebut) & Q(date__lte=datefin) & (
            Q(professeur_firstgroup=prof) | Q(professeur_secondgroup=prof))).count()*3.5
        list.append(annee_and_charge(a['annee_universitaire'] , seance))
    url = re.sub('/annees$', '/', request.path)
    return render(request, 'anne_universitaire_by_teacher.html' , locals())

def generate_PDF_trombinoscope(request ,promotion):
    etudiant = Etudiant.objects.filter(promotion__libelle=promotion).order_by("nom")
    for a in etudiant:
        tag = str(a.image)
        tag = "../" + tag
        print(tag.replace('app', '..'))
        a.image = tag

    semestre = Semestre.objects.filter(promotion__libelle =promotion).first()
    template = get_template('trombinoscope.html')
    html  = template.render(locals())
    file = open('pdf.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
            encoding='utf-8')
    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, 'application/pdf')
