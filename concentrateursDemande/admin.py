from django.contrib import admin

from .models import Demande, Concentrateur, DemandeTraite

admin.site.register(Demande)
admin.site.register(Concentrateur)
admin.site.register(DemandeTraite)