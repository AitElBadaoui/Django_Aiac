from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import authenticate

from app.models import Matiere , Seance, Professeur
from django.utils.translation import ugettext as _

class SeanceForm1(forms.ModelForm):

    class Meta:
        model = Seance
        fields = ['matiere','professeur_firstgroup','is_two','professeur_secondgroup','salle','activite','avancement']
        widgets = {
                        'matiere': forms.Select(attrs={'class': 'matiere'}),
        }

    def __init__(self, *args, **kwargs):
        super(SeanceForm1, self).__init__(*args, **kwargs)
        self.fields['matiere'].empty_label = "-LIBRE-"

class UserForm(forms.Form):
    username = forms.CharField(label="Email" , widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username = username , password= password)
        if not user :
            raise forms.ValidationError(_("Le nom d'utilisateur ou le mot de passe que vous avez entré n'est pas valide"))
        if not user.is_active:
            raise forms.ValidationError(_("le compte est désacitvé "))
        return super(UserForm,self).clean()