from django.urls import path
from . import views

urlpatterns = [
    path('', views.DemandeClient, name='demande_client'),
    path('index_admin/', views.IndexAdmin, name='index_admin'),
    path('admin_concentrateur/', views.ConcentrateurListe, name='concentrateur_liste'),
    path('admin_demande/', views.ListeDemande, name='liste_demande'),
    path('admin_operations/', views.Operations, name='operations'),

]