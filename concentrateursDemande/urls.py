from django.urls import path
from . import views

urlpatterns = [
    path('', views.DemandeForm, name='demande_concentrateur'),
    path('index_admin/', views.IndexAdmin, name='index_admin'),
    path('admin_concentrateur/', views.AdminConcentrateur, name='admin_concentrateur'),
    path('admin_demande/', views.AdminDemande, name='admin_demande'),
    path('admin_operations/', views.AdminOperations, name='admin_operations'),

]