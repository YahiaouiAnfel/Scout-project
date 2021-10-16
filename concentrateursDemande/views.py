from django.shortcuts import render
from .forms import DemandeClientFormulaire,ConcentrateurAddForm, DemandeTraiteForm, RetourConcentrateur
from .models import Concentrateur, Demande, DemandeTraite

def DemandeClient(request):
	if request.method == "POST":
		form = DemandeClientFormulaire(request.POST)
		if form.is_valid():
			form.save()
			form = DemandeClientFormulaire()
	else:
		form = DemandeClientFormulaire()
	return render(request,'index.html', {'form': form})


def IndexAdmin(request):
	return render(request,'index_admin.html')


def ConcentrateurListe(request):
	if request.method == "POST":
		form = ConcentrateurAddForm(request.POST)
		if form.is_valid():
			form.save()
			form = ConcentrateurAddForm()
	else:
		form = ConcentrateurAddForm()
	concentrateur = Concentrateur.objects.filter()
	return render(request,'concentrateur_liste.html', {'form': form,'concentrateur':concentrateur})


def ListeDemande(request):
	if request.method == "POST":
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
	else:
		form = DemandeTraiteForm()
	demande = Demande.objects.filter()
	return render(request,'demande_client.html', {'demande':demande,'form':form})


def Operations(request):
	if request.method == "POST":
		form2 = RetourConcentrateur(request.POST)
		if form2.is_valid():
			concentrateur = Concentrateur.objects.get(Reference=form2.cleaned_data.get("concentrateur"))
			concentrateur.disponible = '2'
			concentrateur.save()
			demande = Demande.objects.get(NCI=form2.cleaned_data.get("demande"))
			demandeTraite = DemandeTraite.objects.get(demande=demande,concentrateur=form2.cleaned_data.get("concentrateur"))
			demandeTraite.dateRetour = form2.cleaned_data.get("dateRetour")
			demandeTraite.save()
			form2 = RetourConcentrateur()
	else:
		form2 = RetourConcentrateur()

	operations = DemandeTraite.objects.filter()
	return render(request,'operations.html', {'operations':operations,'form2':form2})
