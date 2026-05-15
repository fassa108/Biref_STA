from .models import Entree
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender= Entree)
def notification_Entree(sender, instance, created, **kwargs):
    if created :
        titre_entree = instance.titre
        auteur_entree = instance.user
        categorie = instance.categorie
        
        print(f"Nouveau journal de {auteur_entree} : {titre_entree} de categorie {categorie}")