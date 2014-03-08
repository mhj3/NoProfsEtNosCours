from django.contrib import admin
from parametrebase.models import Etablissement, CodeCours, CodePrograme, Professeur, Cours
# Register your models here.

class EtablissementAdmin(admin.ModelAdmin):
    list_display=('Nom','Lieu');
    search_fields = ('Nom',)

class CoursAdmin(admin.ModelAdmin):
    list_display = ('titre','credits','lieu','public_cible','pre_requis','objectif','description','evaluation')
    list_filter = ('titre','lieu',)
    ordering = ('-titre',)
    fields = ('codecours','codeprogram','prof','titre','credits','lieu','public_cible','pre_requis','objectif','description','plan','forma','ressource','evaluation')
    filter_horizontal = ('prof',)
    search_fields = ('titre',)

admin.site.register(Etablissement,EtablissementAdmin)
admin.site.register(CodeCours)
admin.site.register(CodePrograme)
admin.site.register(Professeur)
admin.site.register(Cours, CoursAdmin)