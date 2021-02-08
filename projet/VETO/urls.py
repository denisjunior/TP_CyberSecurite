from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='index'),

    path('medecin/create', views.medecin, name='create_medecin'),
    path('medecin/update/<int:pk>/', views.medecin_update, name='updateM'),
    path('medecin/delete/<int:pk>/', views.medecin_delete, name='deleteM'),

    path('parent', views.parent, name='create_parent'),
    path('parent/update/<int:pk>/', views.parent_update, name='updateParent'),
    path('parent/delete/<int:pk>/', views.parent_delete, name='deleteParent'),

    path('type', views.typeanimal, name='create_type'),
    path('type/update/<int:pk>/', views.typeanimal_update, name='updateType'),
    path('type/delete/<int:pk>/', views.typeanimal_delete, name='deleteType'),


    path('animal', views.animal, name='create_animal'),
    path('animal/update/<int:pk>/', views.animal_update, name='updateAnimal'),
    path('animal/delete/<int:pk>/', views.animal_delete, name='deleteAnimal'),


    path('rdv', views.rendezvous, name='create_rdv'),
    path('rdv/update/<int:pk>/', views.rendezvous_update, name='updateRdv'),
    path('rdv/delete/<int:pk>/', views.rendezvous_delete, name='deleteRdv'),


    path('medicament', views.medicament, name='create_medicament'),
    path('medicament/update/<int:pk>/', views.medicament_update, name='updateMedicament'),
    path('medicament/delete/<int:pk>/', views.medicament_delete, name='deleteMedicament'),

    path('ordonnance', views.ordonnance, name='create_ordonnance'),
    path('ordonnance/delete/<int:pk>/', views.ordonnance_delete, name='deleteOrdonnance'),

    path('prescription', views.prescription, name='create_prescription'),
    path('prescription/update/<int:pk>/', views.prescription_update, name='updatePrescription'),
    path('prescription/delete/<int:pk>/', views.prescription_delete, name='deletePrescription'),
]