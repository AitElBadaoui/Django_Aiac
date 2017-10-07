from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.accueil, name="accueil"),
    url(r'^accueil/$', views.index , name='index'),
    url(r'^emploi_du_temps/(?P<promotion>\w+)/(?P<semestre>\w+)/(?P<semaine>\d+)', views.emploi_du_temps_courant_add),
    url(r'^emploi_du_temps/', views.emploi_du_temps_courant , name="emploi_courant"),
    url(r'^emploi_du_temps_archive/$', views.emploi_du_temps_archive_list, name="emploi_courant_archive"),
    url(r'^emploi_du_temps_archive/(?P<promotion>\w+)/(?P<semestre>\w+)/(?P<semaine>\d+)', views.emploi_du_temps_archive, name="emploi_courant_archive_info"),

    url(r'^emploi_pdf/$', views.imprimer , name="imprimer"),


    url(r'^repertoire_telephonique_prof/$' , views.repertoire_prof , name="repertoire_prof"),
    url(r'^repertoire_telephonique_etudiant/$' , views.repertoire_etud , name="repertoire_etud"),


    url(r'professeurs/$', views.prof , name="prof"),
    url(r'professeurs/(?P<id>\d+)/annees$', views.annee , name="anne"),
    url(r'professeurs/(?P<id>\d+)/$', views.mois , name="mois"),
    url(r'professeurs/(?P<id>\d+)/(?P<month>\w+)/(?P<year>\d+)/$', views.facture , name="facture"),
    url(r'professeurs/(?P<id>\d+)/(?P<month>\w+)/(?P<year>\d+)/fiche$', views.fiche , name="fiche2"),
    url(r'professeurs/(?P<id>\d+)/(?P<month>\w+)/(?P<year>\d+)/modif/(?P<matiere>\d+)/fiche_modif$', views.fiche_modif, name="fiche2_modif"),
    url(r'professeurs/(?P<id>\d+)/(?P<month>\w+)/(?P<year>\d+)/(?P<matiere>\d+)/$', views.facturation , name="fiche2"),
    url(r'professeurs/(?P<id>\d+)/(?P<month>\w+)/(?P<year>\d+)/modif/(?P<matiere>\d+)/$', views.facturation_modif , name="fiche2"),
    url(r'professeurs/(?P<id>\d+)/(?P<month>\w+)/(?P<year>\d+)/modif/(?P<matiere>\d+)/modif$', views.facturation_modif_memoire),
    url(r'professeurs/(?P<id>\d+)/(?P<month>\w+)/(?P<year>\d+)/modif/(?P<matiere>\d+)/modif/done$', views.facturation_modif_done , name="envoi_modif"),
    url(r'professeurs/(?P<id>\d+)/(?P<month>\w+)/(?P<year>\d+)/(?P<matiere>\d+)/fiche$', views.fichee , name="Memo_vacation"),
    url(r'professeurs/(?P<id>\d+)/(?P<month>\w+)/(?P<year>\d+)/no', views.no , name="fiche2"),

    #Matieres:
    url(r'matieres/$', views.promotion_list , name="matiere"),
    url(r'matieres/(?P<promotion>\w+)/$' , views.semestre_list , name="semestre_list_matiere"),
    url(r'matieres/(?P<promotion>\w+)/(?P<semestre>\w+)$' , views.matiere , name="Matiere_list"),
    url(r'matieres/(?P<promotion>\w+)/(?P<semestre>\w+)/fiche$' , views.fiche_matiere , name="fiche_etats_matiere"),

    #Etudiant:
    url(r'^etudiants/$', views.promotion_list, name="gestion_etudiant"),
    url(r'^etudiants/(?P<promotion>\w+)/$', views.gestion_etudiant),
    url(r'^etudiants/(?P<promotion>\w+)/(?P<cin>\w+)/$', views.fiche_renseignement),
    url(r'^etudiants/(?P<promotion>\w+)/(?P<cin>\w+)/profile/$', views.generate_PDF , name="fiche_profil"),
    url(r'^etudiants/(?P<promotion>\w+)/trombinoscope/fiche$', views.generate_PDF_trombinoscope),
    #logout
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'verouille/$', views.verrou , name="verrou"),
    url(r'check/$', views.check_login , name="check"),

   # url(r'facture/(?P<id>\d+)$', views.facture,name="facture"),
    #url(r'^facture/(?P<professeur_id>$', views.facture , name="facture"),

    url(r'^getProf/$' , views.getProf ),
    url(r'^vide/$' , views.getVide ),
    url(r'^getSeance/$' , views.getSeance ),
    url(r'^getMatiere/$' , views.getMatiere ),

    url(r'^events/$', views.event, name="events_drag"),
    url(r'^edit/$', views.edit, name="edit"),
    url(r'^edit_title/$', views.edit_info, name="editTitle"),
    url(r'^add_event/$', views.addEvent, name="addevent"),
    url(r'^tuto/$', views.tuto, name="tuto"),

    url(r'^emploi_du_temps/(?P<promotion>\w+)/(?P<semestre>\w+)/(?P<semaine>\d+)/getSeance/(?P<num>\w+)/$' , views.getSeance),
]