from covoiturage.models import Trajet
from covoiturage.models import Reservation

import pytest

def test_creation_d_un_trajet(db):
    trajet = Trajet.objects.create(
        conducteur = "Abdel",
        ville_depart = "Sokode",
        ville_arrivee = "Lome",
        heure_depart = "19:00",
        date_depart = "2000-02-12",
        places = 4 ,
        prix_par_place = 10000
    )
    
    assert trajet.conducteur
    assert trajet.ville_arrivee
    assert trajet.heure_depart
    assert trajet.places
    assert trajet.prix_par_place
    assert trajet.ville_depart
    assert trajet.date_depart
    
    
def test_trajet_a_au_moins_une_place(db):
    with pytest.raises(Exception):
        trajet = Trajet.objects.create(
            conducteur = "Abdel",
            ville_depart = "Sokode",
            ville_arrivee = "Lome",
            heure_depart = "19:00",
            date_depart = "2000-02-12",
            places = 0 ,
            prix_par_place = 10000
    )
        
def test_affichage_trajet(db):
   trajet = Trajet.objects.create(
        conducteur = "Abdel",
        ville_depart = "Sokodé",
        ville_arrivee = "Lomé",
        heure_depart = "19:00",
        date_depart = "2000-02-12",
        places = 5 ,
        prix_par_place = 10000
    )  
   
   assert str(trajet) == "Sokodé -> Lomé 2000-02-12 à 19:00"     



def test_creation_d_une_reservation(db):
    trajet = Trajet.objects.create(
            conducteur = "Abdel",
            ville_depart = "Sokodé",
            ville_arrivee = "Lomé",
            heure_depart = "19:00",
            date_depart = "2000-02-12",
            places = 5 ,
            prix_par_place = 10000
    )
     
    reservation = Reservation.objects.create(
        trajet = trajet,
        nom_passager = "Abouraima",
        nombre_place = 5,
    )
    
    assert reservation.trajet
    assert reservation.nom_passager    
    assert reservation.nombre_place 
    
    
def test_affichage_trajet(db):
    trajet = Trajet.objects.create(
        conducteur = "Abdel",
        ville_depart = "Sokodé",
        ville_arrivee = "Lomé",
        heure_depart = "19:00",
        date_depart = "2000-02-12",
        places = 5 ,
        prix_par_place = 10000
)
        
    reservation = Reservation.objects.create(
        trajet = trajet,
        nom_passager = "Abouraima",
        nombre_place = 5,
    )
   
    assert str(reservation) == "Abouraima : 5 places"     
    
    
    
def test_passager_peux_pas_avoir_2_trajet(db):
    trajet = Trajet.objects.create(
        conducteur = "Abdel",
        ville_depart = "Sokodé",
        ville_arrivee = "Lomé",
        heure_depart = "19:00",
        date_depart = "2000-02-12",
        places = 5 ,
        prix_par_place = 10000
    )
            
    reservation = Reservation.objects.create(
        trajet = trajet,
        nom_passager = "Abouraima",
        nombre_place = 5,
    )
    
    with pytest.raises(Exception):
        reservation = Reservation.objects.create(
            trajet = trajet,
            nom_passager = "Abouraima",
            nombre_place = 5,
        )
        
        
        
        
        
        