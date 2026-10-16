from covoiturage.models import Trajet
import pytest

def test_creation_d_un_trajet(db):
    trajet = Trajet.objects.create(
        conducteur = "Abdel",
        ville_depart = "Sokode",
        ville_arrivee = "Lome",
        heure_depart = "19:00",
        date_depart = "12-02-2000",
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
            date_depart = "12-02-2000",
            places = 0 ,
            prix_par_place = 10000
    )
        
def test_affichage_trajet(db):
   trajet = Trajet.objects.create(
        conducteur = "Abdel",
        ville_depart = "Sokodé",
        ville_arrivee = "Lomé",
        heure_depart = "19:00",
        date_depart = "12-02-2000",
        places = 0 ,
        prix_par_place = 10000
    )  
   
   assert str(trajet) == "Sokodé -> Lomé 12-02-2000 à 19:00"     
        
        