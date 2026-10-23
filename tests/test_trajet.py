from covoiturage.models import Trajet
from covoiturage.models import Reservation
import datetime

import pytest

@pytest.fixture
def trajet_1(db):
    trajet = Trajet.objects.create(
        conducteur = "Abdel",
        ville_depart = "Sokodé",
        ville_arrivee = "Lomé",
        heure_depart = "19:00",
        date_depart = "2000-02-12",
        places = 5 ,
        prix_par_place = 10000
    ) 
    return trajet 

@pytest.fixture
def trajet_futur(db):
    trajet = Trajet.objects.create(
        conducteur = "Abdelaa",
        ville_depart = "Sokodé",
        ville_arrivee = "Lomé",
        heure_depart = "19:00",
        date_depart = "2027-02-12",
        places = 5 ,
        prix_par_place = 10000
    ) 
    return trajet 


def test_creation_d_un_trajet(db,trajet_1):
    trajet = trajet_1
    
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
        
def test_affichage_trajet(db,trajet_1):
   trajet = trajet_1 
   
   assert str(trajet) == "Sokodé -> Lomé 2000-02-12 à 19:00"     



def test_creation_d_une_reservation(db,trajet_1):
    trajet = trajet_1
     
    reservation = Reservation.objects.create(
        trajet = trajet,
        nom_passager = "Abouraima",
        nombre_place = 5,
    )
    
    assert reservation.trajet
    assert reservation.nom_passager    
    assert reservation.nombre_place 
    
    
def test_affichage_trajet(db,trajet_1):
    trajet = trajet_1
        
    reservation = Reservation.objects.create(
        trajet = trajet,
        nom_passager = "Abouraima",
        nombre_place = 5,
    )
   
    assert str(reservation) == "Abouraima : 5 places"     
    
    
    
def test_passager_peux_pas_avoir_2_trajet(db,trajet_1):
    trajet = trajet_1
            
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
        
        
def test_page_liste_trajet_sa_affiche_bien(client,db,trajet_1):
    response = client.get("/trajet/index")
    assert "Abdel" in response.text     
    assert "Sokodé" in response.text  
    assert "9:00" in response.text  
    assert "2000-02-12" in response.text  
    assert "Lomé" in response.text  
        
        
def test_montrer_que_les_trajet_a_venir(db, client ,trajet_1,trajet_futur):
    response = client.get("/trajet/index")    
    assert trajet_1.date_depart not in response.text
    assert trajet_futur.date_depart in response.text
    
def test_les_trajet_sont_ordonner(db, client ,trajet_1,trajet_futur):
    response = client.get("/trajet/index")   
    
    date1_idx = response.find(trajet_1.date)
    date2_idx = response.find(trajet_futur.date)
    
    assert date1_idx < date2_idx 
    
    
    
    