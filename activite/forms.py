from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Entree


class EntreeForm(forms.ModelForm):
    class Meta:
        model = Entree
        fields = ['titre','contenu_textuel', 'categorie', 'image_de_preuve']

class EntreeUpdateForm(forms.ModelForm):
    class Meta:
        model = Entree
        fields = ['titre','contenu_textuel', 'categorie', 'image_de_preuve','etat']


class UCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']