from django.contrib import admin
from .models import Matiere,Professeur,Seance,Semestre, EmploiDuTemps , Etudiant, Diplome , Promotion


class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ('nom','matiere')

class PromotionAdmin(admin.ModelAdmin):
   list_display   = ('libelle',)
   list_filter    = ('libelle',)
   ordering       = ('libelle',)
   search_fields  = ('libelle',)

admin.site.register(Promotion, PromotionAdmin)

class ProfesseurAdmin(admin.ModelAdmin):
   list_display   = ('nom' , 'prenom', 'diplome' , 'grade' , 'type', 'telephone' )
   list_filter    = ('nom' , 'prenom' , 'grade', 'diplome' , 'type', 'telephone' )
   ordering       = ('nom',)
   search_fields  = ('nom' , 'prenom' , 'grade', 'diplome' , 'type', 'telephone' , 'matiere')

admin.site.register(Professeur, ProfesseurAdmin)

class MatiereAdmin(admin.ModelAdmin):
   list_display   = ('libelle' , 'chargeHoraire', 'chargeRealise' , 'seanceRealise' , 'semestre')
   list_filter    = ('libelle' , 'chargeHoraire', 'chargeRealise' , 'seanceRealise' , 'semestre')
   ordering       = ('semestre',)
   search_fields  = ('libelle' , 'chargeHoraire', 'chargeRealise' , 'seanceRealise' , 'semestre')

admin.site.register(Matiere, MatiereAdmin)

class SemestreAdmin(admin.ModelAdmin):
   list_display   = ('libelle' , 'annee_universitaire', 'dateDebut' , 'dateFin' , 'promotion')
   list_filter    = ('libelle' , 'annee_universitaire', 'dateDebut' , 'dateFin' , 'promotion')
   ordering       = ('promotion',)
   search_fields  = ('libelle' , 'annee_universitaire', 'dateDebut' , 'dateFin' , 'promotion')


admin.site.register(Semestre , SemestreAdmin)

class DiplomeAdmin(admin.ModelAdmin):
   list_display   = ('libelle' , 'taux_brut', 'taux_net')
   list_filter    = ('libelle' , 'taux_brut', 'taux_net')
   ordering       = ('libelle',)
   search_fields  = ('libelle' , 'taux_brut', 'taux_net')

admin.site.register(Diplome , DiplomeAdmin)

class EtudiantAdmin(admin.ModelAdmin):
   list_display   = ('promotion' , 'nom' , 'prenom', 'cin' , 'lieu_naissance' , 'mail' , 'tel')
   list_filter    = ('promotion' , 'nom' , 'prenom', 'cin' , 'lieu_naissance' , 'mail' , 'tel')
   ordering       = ('promotion',)
   search_fields  = ('promotion' , 'nom' , 'prenom', 'cin' , 'lieu_naissance' , 'mail' , 'tel')

admin.site.register(Etudiant , EtudiantAdmin)

