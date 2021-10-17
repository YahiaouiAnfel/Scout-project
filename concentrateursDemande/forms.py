from django import forms
from .models import Demande, Concentrateur, DemandeTraite
from django.conf import settings
import datetime
from datetime import date
import django.utils
from django.utils import timezone, dateformat

class DemandeClientFormulaire(forms.ModelForm):

    class Meta:
        model = Demande
        widgets = {
          'autre': forms.Textarea(attrs={'rows':5}),
        }
        fields = ('NCI','nomPrenom', 'Age', 'numeroTel', 'commune', 'adresse', 'poids', 'oxygene', 'ordonnance', 'medecin', 'NumMedecin', 'endroit', 'maladieChronique', 'autre','traite')



class ConcentrateurAddForm(forms.ModelForm):

    class Meta:
        model = Concentrateur
        widgets = {
          'autre': forms.Textarea(attrs={'rows':2}),
        }
        fields = ('Reference','Debit', 'pression', 'electrique', 'concentration', 'sonore', 'dimensions', 'poids', 'soupage','autre', 'disponible')



class DemandeTraiteForm(forms.ModelForm):

    class Meta:
        model = DemandeTraite
        fields = ('demande','concentrateur', 'date')



class RetourConcentrateur(forms.Form):
    demande=forms.ModelChoiceField(DemandeTraite.objects.filter(dateRetour=None),label='رقم بطاقة التعريف')
    concentrateur=forms.ModelChoiceField(Concentrateur.objects.filter(disponible='1'),label='الرقم التسلسلي')
    dateRetour=forms.DateField(label='تاريخ إعادة المكثف', initial=dateformat.format(timezone.now(), 'Y-m-d'), input_formats=settings.DATE_INPUT_FORMATS)