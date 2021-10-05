from django import forms

from .models import Demande, Concentrateur, DemandeTraite

class DemandeFormulaire(forms.ModelForm):

    class Meta:
        model = Demande
        widgets = {
          'autre': forms.Textarea(attrs={'rows':2}),
        }
        fields = ('NCI','nomPrenom', 'Age', 'numeroTel', 'commune', 'adresse', 'poids', 'oxygene', 'ordonnance', 'endroit', 'maladieChronique', 'autre','traite')



class ConcentrateurForm(forms.ModelForm):

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
    concentrateur=forms.ModelChoiceField(Concentrateur.objects.filter(disponible='1'),label='الرقم التسلسلي')