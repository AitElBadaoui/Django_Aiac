from django.db import models
from datetime import timezone
import os
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, username,password=None):
        if not username:
            raise ValueError("L'utilisateur doit avoir un nom d'utilisateur")

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        if not username :
            raise ValueError("L'utilisateur doit avoir un nom d'utilisateur")

        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.is_active = 1
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_verrou = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    class Meta:
        verbose_name = _('utilisateur')

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        # Will not be asking for anything not admin related anyway
        return self.is_admin

    def has_module_perms(self, app_label):
        # Will not be asking for anything not admin related anyway
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin


class Promotion(models.Model):
    libelle = models.CharField(max_length=50)
    def __str__(self):
        return self.libelle

class Semestre(models.Model):
    libelle = models.CharField(max_length=50)
    annee_universitaire = models.CharField(_("Année univérsitaire") , max_length=60 )
    dateDebut = models.DateField(_("Date de Début"))
    dateFin = models.DateField(_("Date de Fin"))
    promotion = models.ForeignKey(Promotion , on_delete=models.SET_NULL , null =True)
    is_full = models.BooleanField(default=False)

    def __str__(self):
        return self.libelle + ' » ' + str(self.promotion)

class Semaine(models.Model):
    num_semaine = models.PositiveIntegerField()
    dateDebut = models.DateField(_("Date de Début"))
    dateFin = models.DateField(_("Date de Fin"))
    semestre = models.ForeignKey(Semestre , on_delete=models.CASCADE , null=True)

    def __str__(self):
        return str(self.dateDebut) + "-" + str(self.dateFin)

class Matiere(models.Model):
    libelle = models.CharField(max_length=100)
    chargeHoraire = models.PositiveIntegerField(null=True)
    chargeRealise = models.PositiveIntegerField(null=True)
    seanceRealise = models.PositiveIntegerField(null=True)
    semestre = models.ForeignKey(Semestre,on_delete=models.SET_NULL , null=True)

    def __str__(self):
        return self.libelle

class Diplome(models.Model):
    libelle = models.CharField(max_length=50)
    taux_brut = models.DecimalField(max_digits=5, decimal_places=2 , null=True)
    taux_net = models.DecimalField(max_digits=5, decimal_places=2 , null=True)
    def __str__(self):
        return self.libelle
class Professeur(models.Model):
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=60)
    grade = models.CharField(max_length=60 , null =True , blank=True)
    diplome = models.ForeignKey(Diplome , on_delete=models.CASCADE , null=True)
    type = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30 , default="06")
    matiere = models.ManyToManyField(Matiere)

    def __str__(self):
        return self.nom

class EmploiDuTemps(models.Model):
    semaine = models.ForeignKey(Semaine , on_delete=models.CASCADE, null=True)
    dateDebut = models.DateField(_("Date de Début"))
    dateFin = models.DateField(_("Date de Fin"))
    isValid =  models.BooleanField(default=False)
    codeEmploi = models.CharField(max_length=30)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, null=True)
    observation = models.CharField(max_length=500 , blank=True , null=True)

    def __str__(self):
        return self.codeEmploi

    def code_Emploi(self):
        anne = self.semestre.annee_universitaire.split("/")
        return "EDT_"+str(self.semestre.promotion)+"_"+"S"+str(self.semaine.num_semaine)+"_"+str(anne[1])

class Seance(models.Model):
    num_seance = models.PositiveIntegerField(blank=True , null=True)
    matiere = models.ForeignKey(Matiere,on_delete=models.SET_NULL, related_name="Matieres" ,null=True, blank=True)
    avancement = models.CharField(max_length=20, blank=True , null=True)
    professeur_firstgroup= models.ManyToManyField(Professeur , blank=True , related_name='Professeur')
    professeur_secondgroup = models.ManyToManyField(Professeur, blank=True , related_name='+')
    emploi = models.ForeignKey(EmploiDuTemps , on_delete=models.SET_NULL , null=True)
    salle = models.CharField(max_length=30 ,blank=True , null=True)
    activite = models.CharField(max_length=60 ,blank=True , null=True)
    is_two = models.BooleanField(default=False)
    date = models.DateField(_('date seance'), default='1996-03-23')
    def __str__(self):
        return str(self.num_seance)

class Etudiant(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    cin = models.CharField(max_length=30)
    cne = models.PositiveIntegerField
    date_naissance = models.DateField('date de naissance')
    date_entree = models.DateField('date d entrée',null=True)
    lieu_naissance = models.CharField(max_length=30,null=True)
    adresse_residence = models.CharField('adresse de residence', max_length=255)
    mail = models.EmailField(default='a@exemple.com')
    tel = models.PositiveIntegerField(default='0')
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, null=True)
    num_carte_stagiaire=models.CharField(max_length=30,null=True,blank=True)
    bac=models.CharField(max_length=100,null=True)
    mention= models.CharField(max_length=100, null=True , verbose_name="Mention Bac")
    filiere=models.CharField(max_length=100,null=True)
    Classement=models.CharField(max_length=100,null=True)
    Cne = models.CharField(max_length=25)
    etablissement=models.CharField(max_length=100,null=True)
    datevalidation_premiere_annee=models.DateField(blank=True,default='2017-10-20')
    datevalidation_s3=models.DateField(blank=True,default='2017-10-20')
    datevalidation_deuxieme_annee=models.DateField(blank=True,default='2017-10-20')
    image = models.FileField(upload_to='app/static/img')

    def age(self):
        now = timezone.now()
        born = self.date_naissance
        return now.year - born.year - ((now.month, now.day) < (born.month, born.day))

    def __str__(self):
        return str(self.cin)

    def filename(self):
        return os.path.basename(self.image.name)

class Horaire_semaine(models.Model):
    libelle = models.CharField(max_length=50)
    dateDebut = models.DateField()
    dateFin = models.DateField()

class Semaine_facture(models.Model):
    seance = models.ForeignKey(Seance , on_delete=models.CASCADE , null=True)
    horaire_semaine = models.ForeignKey(Horaire_semaine , on_delete=models.CASCADE , null=True)

class Horaire_jour(models.Model):
    lundi = models.CharField(max_length=6 , null=True)
    Mardi = models.CharField(max_length=6 , null=True)
    Mercredi = models.CharField(max_length=6 , null=True)
    Jeudi = models.CharField(max_length=6 , null=True)
    Vendredi = models.CharField(max_length=6 , null=True)
    Samedi = models.CharField(max_length=6 , null=True)
    lundi_modif = models.CharField(max_length=6 , null=True)
    Mardi_modif  = models.CharField(max_length=6 , null=True)
    Mercredi_modif  = models.CharField(max_length=6 , null=True)
    Jeudi_modif  = models.CharField(max_length=6 , null=True)
    Vendredi_modif  = models.CharField(max_length=6 , null=True)
    Samedi_modif  = models.CharField(max_length=6 , null=True)
    horaire_semaine = models.ForeignKey(Horaire_semaine, on_delete=models.CASCADE, null=True)
    professeur = models.ForeignKey(Professeur , on_delete=models.CASCADE , null=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE , null=True)
    total = models.DecimalField(max_digits=4 , decimal_places=1 , default=0.0)
    total_modif = models.DecimalField(max_digits=5 , decimal_places=1 , default=0.0)
class Events(models.Model):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=7 , null=True)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
