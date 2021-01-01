from django.db import models

# Create your models here.
class TypeAnimal(models.Model):
    libelleType = models.CharField(max_length=100)

    def __str__(self):
        return self.libelleType

class Parent(models.Model):
    nomParent       = models.CharField(max_length=100)
    prenomParent    = models.CharField(max_length=100)
    contactP        = models.IntegerField(default=None)
    def __str__(self):
        return self.nomParent

class Medecin(models.Model):
    nomMedecin      = models.CharField(max_length=100)
    prenomMedecin   = models.CharField(max_length=100)
    contactMedcin   = models.IntegerField(default=None)
    def __str__(self):
        return self.nomMedecin

class Animal(models.Model):
    nomAnimal       = models.CharField(max_length=100)
    sexAnimal       = models.CharField(max_length=1)
    parent_animal   = models.ForeignKey(Parent, on_delete=models.CASCADE)
    type_animal     = models.ForeignKey(TypeAnimal, on_delete=models.CASCADE)
    def __str__(self):
        return self.nomAnimal

class Rendezvous(models.Model):
    dateRdv         = models.DateField(auto_now=False)
    heureDebut      = models.TimeField(default=None)
    heureFin        = models.TimeField(default=None)
    medecin_rdv     = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    animal_rdv      = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.animal_rdv.nomAnimal

class Medicament(models.Model):
    nomMedicament   = models.CharField(max_length=100)
    description     = models.CharField(max_length=100)

    def __str__(self):
       return self.nomMedicament

class Ordonnance(models.Model):
    rdv_ord         = models.ForeignKey(Rendezvous, on_delete=models.CASCADE)

class Prescription(models.Model):
    datePres        = models.DateField(auto_now=False)
    frequence       = models.CharField(max_length=100)
    quantite        = models.IntegerField(default=None)
    ordonnance_pres = models.ForeignKey(Ordonnance, on_delete=models.CASCADE)
    medicament_pres = models.ForeignKey(Medicament, on_delete=models.CASCADE)
