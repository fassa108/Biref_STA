from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Categorie(models.Model) :
    nom_categorie = models.CharField( max_length=64)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_categorie

class Entree(models.Model) :
    class Statut(models.TextChoices):
        EN_COURS = 'en_cours', 'En cours'
        RESOLU   = 'resolu',   'Résolu'
        BLOQUE   = 'bloque',   'Bloqué'

    titre = models.CharField( max_length=100)
    contenu_textuel = models.TextField()
    image_de_preuve = models.ImageField(upload_to='images/')
    date_creation = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    etat = models.CharField(
        max_length=20,
        choices=Statut.choices,
        default=Statut.EN_COURS
    )