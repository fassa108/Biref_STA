from django.contrib import admin

from activite.models import Categorie, Entree

# Register your models here.
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom_categorie','description')
    search_fields = ('nom_categorie',)
    list_filter = ('date_creation',)

admin.site.register(Categorie, CategorieAdmin)

class EntreeAdmin(admin.ModelAdmin):
    list_display = ('titre','contenu_textuel','image_de_preuve','date_creation', 'categorie','user')
    search_fields = ('titre','user')
    list_filter = ('date_creation',)

admin.site.register(Entree, EntreeAdmin)

