from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import ProtectedError

# Create your views here.
def medecin(request):
    all_medecin = Medecin.objects.all()
    if request.method == 'POST':
        form = MedecinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enregistrement effectuer avec succès')
        else:
            messages.error(request,'une erreur est survenue veuillez réessayer (Un medecin avec ce nom existe probablement déjà)')
            return render(request, 'medecin/createMe.html',{"form":form, "medecins":all_medecin})
    ctx =   {"medecins":all_medecin}
    return render(request, 'medecin/createMe.html', ctx)

def medecin_update(request, pk):
    medecin = Medecin.objects.get(pk=pk)
    medecins= Medecin.objects.all()
    if request.method == 'POST':
        form = MedecinForm(request.POST, instance=medecin)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification effectuer avec succès')
        else:
            return render(request, 'medecin/updateMe.html', {"form":form, "medecins":medecins, "medecin":medecin})
    ctx = {"medecins":medecins, "medecin":medecin}
    return render(request, 'medecin/updateMe.html', ctx)

def medecin_delete(request, pk):
    medecins = Medecin.objects.get(pk=pk)
    try:
        medecins.delete()
    except ProtectedError:
        messages.error(request, 'Vous ne pouvez pas supprimer cette Zone')
    else:
        messages.success(request, 'Suppression effectuer avec succès')
    return redirect('create_medecin')

######## parent ############
def parent(request):
    all_parent  = Parent.objects.all()
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enregistrement effectuer avec succès')
        else:
            messages.error(request,'une erreur est survenue veuillez réessayer (Un parent avec ce nom existe probablement déjà)')
            return render(request, 'parent/createParent.html',{"form":form, "parents":all_parent})
    ctx =   {"parents":all_parent}
    return render(request,'parent/createParent.html', ctx)

def parent_update(request, pk):
    parent = Parent.objects.get(pk=pk)
    parents = Parent.objects.all()
    if request.method == 'POST':
        form = ParentForm(request.POST, instance=parent)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification effectuer avec succès')
        else:
            return render(request, 'medecin/updateMe.html', {"form": form, "parents": parents, "parent": parent})
    ctx = {"parents": parents, "parent": parent}
    return render(request, 'parent/updateParent.html', ctx)

def parent_delete(request, pk):
    parents = Parent.objects.get(pk=pk)
    try:
        parents.delete()
    except ProtectedError:
        messages.error(request, 'Vous ne pouvez pas supprimer ce parent')
    else:
        messages.success(request, 'Suppression effectuer avec succès')
    return redirect('create_parent')

###### Type animal ########

def typeanimal(request):
    all_type    = TypeAnimal.objects.all()
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enregistrement effectuer avec succès')
        else:
            messages.error(request,'une erreur est survenue veuillez réessayer (Un type avec ce nom existe probablement déjà)')
            return render(request, 'typeanimal/createTypeanimal.html',{"form":form, "types":all_type})
    ctx =   {"types":all_type}
    return render(request, 'typeanimal/createTypeanimal.html',ctx)

def typeanimal_update(request,pk):
    type = TypeAnimal.objects.get(pk=pk)
    types = TypeAnimal.objects.all()
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification effectuer avec succès')
        else:
            return render(request, 'typeanimal/updateType.html', {"form": form, "types": types, "type": type})
    ctx = {"types": types, "type": type}
    return render(request, 'typeanimal/updateType.html', ctx)

def typeanimal_delete(request,pk):
    types = TypeAnimal.objects.get(pk=pk)
    try:
        types.delete()
    except ProtectedError:
        messages.error(request, 'Vous ne pouvez pas supprimer ce parent')
    else:
        messages.success(request, 'Suppression effectuer avec succès')
    return redirect('create_type')

###### Animal ######
def animal(request):
    all_animal  = Animal.objects.all()
    parent_animal= Parent.objects.all()
    type_animal = TypeAnimal.objects.all()
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enregistrement effectuer avec succès')
        else:
            messages.error(request,'une erreur est survenue veuillez réessayer (Un animal avec ce nom existe probablement déjà)')
            return render(request, 'animal/create_animal.html',{"form":form, "animals":all_animal, "parents":parent_animal, "types":type_animal})
    ctx =   {"animals":all_animal, "parents":parent_animal, "types":type_animal}
    return render(request, 'animal/create_animal.html',ctx)

def animal_update(request, pk):
    animal = Animal.objects.get(pk=pk)
    animals = Animal.objects.all()
    parent_animal = Parent.objects.all()
    type_animal = TypeAnimal.objects.all()
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification effectuer avec succès')
        else:
            return render(request, 'animal/updateAnimal.html', {"form": form, "animals": animals, "animal": animal, "parents":parent_animal, "types":type_animal})
    ctx = {"animals": animals, "animal": animal, "parents":parent_animal, "types":type_animal}
    return render(request, 'animal/updateAnimal.html', ctx)

def animal_delete(request, pk):
    animals = Animal.objects.get(pk=pk)
    try:
        animals.delete()
    except ProtectedError:
        messages.error(request, 'Vous ne pouvez pas supprimer ce parent')
    else:
        messages.success(request, 'Suppression effectuer avec succès')
    return redirect('create_animal')

##### Rendez-vous #########
def rendezvous(request):
    all_rendezvous = Rendezvous.objects.all()
    medecin_rdv = Medecin.objects.all()
    animal_rdv = Animal.objects.all()
    if request.method == 'POST':
        form = RdvForm (request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enregistrement effectuer avec succès')
        else:
            messages.error(request,'une erreur est survenue veuillez réessayer (Un animal avec ce nom existe probablement déjà)')
            #return HttpResponse(form.errors.as_json())
            return render(request, 'rendezvous/create_rdv.html',{"form": form, "rendezvous": all_rendezvous, "medecins": medecin_rdv, "animals": animal_rdv})
    ctx = {"rendezvous":all_rendezvous, "medecins": medecin_rdv, "animals": animal_rdv }
    return render(request, 'rendezvous/create_rdv.html',ctx)

def rendezvous_update(request,pk):
    rdv = Rendezvous.objects.get(pk=pk)
    all_rendezvous = Rendezvous.objects.all()
    medecin_rdv = Medecin.objects.all()
    animal_rdv = Animal.objects.all()
    if request.method == 'POST':
        form = RdvForm(request.POST, instance=rdv)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification effectuer avec succès')
        else:
            return render(request, 'rendezvous/updateRdv.html',{"form": form, "rdv": rdv, "rendezvous": all_rendezvous, "medecins": medecin_rdv,"animals": animal_rdv})
    ctx = {"rdv":rdv, "rendezvous": all_rendezvous, "medecins": medecin_rdv,"animals": animal_rdv}
    return render(request, 'rendezvous/updateRdv.html', ctx)

def rendezvous_delete(request,pk):
    rdv = Rendezvous.objects.get(pk=pk)
    try:
        rdv.delete()
    except ProtectedError:
        messages.error(request, 'Vous ne pouvez pas supprimer ce parent')
    else:
        messages.success(request, 'Suppression effectuer avec succès')
    return redirect('create_rdv')


def medicament(request):
    all_medicament = Medicament.objects.all()
    if request.method == 'POST':
        form = MedicamentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enregistrement effectuer avec succès')
        else:
            messages.error(request,'une erreur est survenue veuillez réessayer (Un médicament avec ce nom existe probablement déjà)')
            return render(request, 'medicament/create_medicament.html', {"form": form, "medicaments": all_medicament})
    ctx = {"medicaments": all_medicament}
    return render(request, 'medicament/create_medicament.html',ctx)

def medicament_update(request,pk):
    medicament = Medicament.objects.get(pk=pk)
    medicaments = Medicament.objects.all()
    if request.method == 'POST':
        form = MedicamentForm(request.POST, instance=medicament)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification effectuer avec succès')
        else:
            return render(request, 'medicament/updateMedicament.html', {"form": form, "medicament": medicament, "medicaments": medicaments})
    ctx = {"medicaments": medicaments, "medicament": medicament}
    return render(request, 'medicament/updateMedicament.html', ctx)

def medicament_delete(request,pk):
    medicament = Medicament.objects.get(pk=pk)
    try:
        medicament.delete()
    except ProtectedError:
        messages.error(request, 'Vous ne pouvez pas supprimer ce medicament')
    else:
        messages.success(request, 'Suppression effectuer avec succès')
    return redirect('create_medicament')


def ordonnance(request):
    all_ordonnance = Ordonnance.objects.all()
    rdv            = Rendezvous.objects.all()
    if request.method == 'POST':
        form = OrdForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enregistrement effectuer avec succès')
        else:
            messages.error(request,'une erreur est survenue veuillez réessayer (Une ordonnance avec ce nom existe probablement déjà)')
            # return HttpResponse(form.errors.as_json())
            return render(request, 'ordonnance/create_ord.html',{"form": form, "ordonnance": all_ordonnance, "rendezvous": rdv})
    ctx = {"ordonnance": all_ordonnance, "rendezvous": rdv}
    return render(request, 'ordonnance/create_ord.html', ctx)

def ordonnance_delete(request,pk):
    ord = Ordonnance.objects.get(pk=pk)
    try:
        ord.delete()
    except ProtectedError:
        messages.error(request, 'Vous ne pouvez pas supprimer cette ordonnance')
    else:
        messages.success(request, 'Suppression effectuer avec succès')
    return redirect('create_ordonnance')

def prescription(request):
    all_prescrition = Prescription.objects.all()
    ordonnance_pres = Ordonnance.objects.all()
    medicament_pres = Medicament.objects.all()
    if request.method == 'POST':
        form = PresForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enregistrement effectuer avec succès')
        else:
            messages.error(request,'une erreur est survenue veuillez réessayer (Une ordonnance avec ce nom existe probablement déjà)')
            # return HttpResponse(form.errors.as_json())
            return render(request, 'prescription/create_prescription.html',{"form": form, "ordonnances": ordonnance_pres, "medicaments": medicament_pres, "prescriptions":all_prescrition})
    ctx = {"ordonnances": ordonnance_pres, "medicaments": medicament_pres, "prescriptions":all_prescrition}
    return render(request, 'prescription/create_prescription.html',ctx)

def prescription_update(request,pk):
    presc = Prescription.objects.get(pk=pk)
    ordonnance_pres = Ordonnance.objects.all()
    medicament_pres = Medicament.objects.all()
    all_prescrition = Prescription.objects.all()
    if request.method == 'POST':
        form = PresForm(request.POST, instance=presc)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modification effectuer avec succès')
        else:
            #return HttpResponse(form.errors.as_json())
            return render(request, 'prescription/updatePrescription.html',{"form": form, "ordonnances": ordonnance_pres, "medicaments": medicament_pres,"prescriptions": all_prescrition, "prescription":presc})
    ctx = {"ordonnances": ordonnance_pres, "medicaments": medicament_pres, "prescription":presc, "prescriptions": all_prescrition}
    return render(request, 'prescription/updatePrescription.html', ctx)

def prescription_delete(request,pk):
    prescriptions = Prescription.objects.get(pk=pk)
    try:
        prescriptions.delete()
    except ProtectedError:
        messages.error(request, 'Vous ne pouvez pas supprimer cette prescription')
    else:
        messages.success(request, 'Suppression effectuer avec succès')
    return redirect('create_prescription')