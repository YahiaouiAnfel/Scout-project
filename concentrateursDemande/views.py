from django.shortcuts import render
from .forms import DemandeFormulaire,ConcentrateurForm, DemandeTraiteForm, RetourConcentrateur
from .models import Concentrateur, Demande, DemandeTraite
def DemandeForm(request):
	if request.method == "POST":
		form = DemandeFormulaire(request.POST)
		if form.is_valid():
			form.save()
			form = DemandeFormulaire()
	else:
		form = DemandeFormulaire()
	return render(request,'index.html', {'form': form})


def IndexAdmin(request):
	return render(request,'index_admin.html')


def AdminConcentrateur(request):
	if request.method == "POST":
		form = ConcentrateurForm(request.POST)
		if form.is_valid():
			form.save()
			form = ConcentrateurForm()
	else:
		form = ConcentrateurForm()
	concentrateur = Concentrateur.objects.filter()
	return render(request,'concentrateur_liste.html', {'form': form,'concentrateur':concentrateur})


def AdminDemande(request):
	if request.method == "POST":
		if 'envoi' in request.POST:
			form = DemandeTraiteForm(request.POST)
			if form.is_valid():
				form.save()
				concentrateur = Concentrateur.objects.get(Reference=form.cleaned_data.get("concentrateur"))
				concentrateur.disponible = '1'
				concentrateur.save()
				demande = Demande.objects.get(NCI=form.cleaned_data.get("demande"))
				demande.traite = '2'
				demande.save()
				form = DemandeTraiteForm()
			form2 = RetourConcentrateur()
		else:
			form2 = RetourConcentrateur(request.POST)
			if form2.is_valid():
				concentrateur = Concentrateur.objects.get(Reference=form2.cleaned_data.get("concentrateur"))
				concentrateur.disponible = '2'
				concentrateur.save()
				form2 = RetourConcentrateur()
			form = DemandeTraiteForm()
	else:
		form = DemandeTraiteForm()
		form2 = RetourConcentrateur()
	demande = Demande.objects.filter()
	return render(request,'concentrateur_demande.html', {'demande':demande,'form':form,'form2':form2})


def AdminOperations(request):
	operations = DemandeTraite.objects.filter()
	return render(request,'operations_liste.html', {'operations':operations})
