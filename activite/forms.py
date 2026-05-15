from django import forms
from django.contrib.auth.models import User
from .models import Entree


class EntreeForm(forms.ModelForm):
    class Meta:
        model = Entree
        fields = ['titre','contenu_textuel', 'categorie', 'image_de_preuve']

class EntreeUpdateForm(forms.ModelForm):
    class Meta:
        model = Entree
        fields = ['titre','contenu_textuel', 'categorie', 'image_de_preuve','etat']


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username','email','password']