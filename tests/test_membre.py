import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gestion import gestion_bibliotheque as bl

class TestMembre(unittest.TestCase):
    
    def setUp(objet):
        objet.membre = bl.Membre("Théodore", 15)
        objet.livre_1 = bl.Livre(1, "Dragonlance", "Margaret Weis & Tracy Hickman", 9780593977156,"Mars 1984")
        objet.livre_2 = bl.Livre(2, "Le Hobbit", "J. R. R. Tolkien", 9780345445605,"Septembre 1937")
        objet.livre_3 = bl.Livre(3, "Le seigneur des anneaux", "J. R. R. Tolkien",  9788845292613, "Juillet 1954")

    
    def tester_emprunter_livre(objet):
        print("\nTest (Membre) - Emprunter un livre")

        #État initial
        objet.assertEqual(objet.membre.determiner_nombre_livres_empruntes(), 0, "Problème d'initalisation (Nombre de livres incorrect)")

        #Ajout d'un premier livre
        objet.membre.emprunter_livre(objet.livre_1)
        objet.assertEqual(objet.membre.determiner_nombre_livres_empruntes(), 1, "Livre non ajouté (Nombre de livres incorrect)")

        #Ajout d'un deuxième livre
        objet.membre.emprunter_livre(objet.livre_2)
        objet.assertEqual(objet.membre.determiner_nombre_livres_empruntes(), 2, "Livre non ajouté (Nombre de livres incorrect)")

        #Rajouter le même livre
        objet.membre.emprunter_livre(objet.livre_1)
        objet.assertEqual(objet.membre.determiner_nombre_livres_empruntes(), 2, "Ajout anormal (Nombre de livres incorrect)")

    
    def tester_rapporter_livre(objet):
        print("\nTest (Membre) - Rapporter un livre")
        
        #État initial
        objet.assertEqual(objet.membre.determiner_nombre_livres_empruntes(), 0, "Problème d'initalisation (Nombre de livres incorrect)")

        #Ajout de livres
        objet.membre.emprunter_livre(objet.livre_1)
        objet.membre.emprunter_livre(objet.livre_2)
        objet.assertEqual(objet.membre.determiner_nombre_livres_empruntes(), 2, "Problème d'ajouts (Nombre de livres incorrect)")

        #Rapporter un livre
        objet.membre.rapporter_livre(objet.livre_1)
        objet.assertEqual(objet.membre.determiner_nombre_livres_empruntes(), 1, "Problème de retour (Nombre de livres incorrect)")
        #Rapporter le même livre
        objet.membre.rapporter_livre(objet.livre_1)
        objet.assertEqual(objet.membre.determiner_nombre_livres_empruntes(), 1, "Problème de retour anormal (Nombre de livres incorrect)")
        #Rapporter un livre non-emprunté (3)
        objet.membre.rapporter_livre(objet.livre_3)
        objet.assertEqual(objet.membre.determiner_nombre_livres_empruntes(), 1, "Probléme de retour anormal (Nombre de livres incorrect)")
        #Rapporter le dernier livre
        objet.membre.rapporter_livre(objet.livre_2)
        objet.assertEqual(objet.membre.determiner_nombre_livres_empruntes(), 0, "Problème de retour (Nombre de livres incorrect)")
        #Rapporter un livre quelconque (Liste vide)
   

if __name__ == "__main__":
    unittest.main()