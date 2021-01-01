from django import forms
from .models import *
class MedecinForm(forms.ModelForm):
    class Meta:
        model   =   Medecin
        fields  =   '__all__'

class ParentForm(forms.ModelForm):
    class Meta:
        model   = Parent
        fields  = '__all__'

class TypeForm(forms.ModelForm):
    class Meta:
        model   = TypeAnimal
        fields  = '__all__'
class AnimalForm(forms.ModelForm):
    class Meta:
        model   = Animal
        fields  = '__all__'
class RdvForm(forms.ModelForm):
    class Meta:
        model   = Rendezvous
        fields  = '__all__'
class MedicamentForm(forms.ModelForm):
    class Meta:
        model   = Medicament
        fields  = '__all__'
class OrdForm(forms.ModelForm):
    class Meta:
        model   = Ordonnance
        fields  = '__all__'
class PresForm(forms.ModelForm):
    class Meta:
        model   = Prescription
        fields  = '__all__'