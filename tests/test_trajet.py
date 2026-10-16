from covoiturage.models import Trajet
import pytest

def test_creation_d_un_trajet(db):
    trajet = Trajet.objects.create(
        conducteur = "Abdel",
        ville_depart = "Sokode",
        ville_arrivee = "Lome",
        heure_depart = "19:00",
        places = 4 ,
        prix_par_place = 10000
    )
    
    assert trajet.conducteur
    assert trajet.ville_arrivee
    assert trajet.heure_depart
    assert trajet.places
    assert trajet.prix_par_place
    assert trajet.ville_depart
    
    
def test_trajet_a_au_moins_une_place(db):
    with pytest.raises(Exception):
        trajet = Trajet.objects.create(
            conducteur = "Abdel",
            ville_depart = "Sokode",
            ville_arrivee = "Lome",
            heure_depart = "19:00",
            places = 0 ,
            prix_par_place = 10000
    )
        
        
        
        