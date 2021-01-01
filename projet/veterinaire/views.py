from django.shortcuts import render
from VETO.models import *

def home(request):
    all_medecin = Medecin.objects.all().count()
    all_parent  = Parent.objects.all().count()
    all_animal  = Animal.objects.all().count()
    all_type    = TypeAnimal.objects.all().count()
    return render(request, 'index.html', locals())