

import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gestion import gestion_bibliotheque as bl

class TestBibliotheque(unittest.TestCase):

    def setUp(objet):
        objet.bibliotheque = bl.Bibliotheque()
        objet.membre_1 = bl.Membre("Théodore", 1)
        objet.membre_2 = bl.Membre("Alice", 2)
        objet.membre_3 = bl.Membre("Carlos", 3)
        objet.livre_1 = bl.Livre(1, "Dragonlance", "Margaret Weis & Tracy Hickman", 9780593977156,"Mars 1984")
        objet.livre_2 = bl.Livre(2, "Le Hobbit", "J. R. R. Tolkien", 9780345445605,"Septembre 1937")
        objet.livre_3 = bl.Livre(3, "Le seigneur des anneaux", "J. R. R. Tolkien",  9788845292613, "Juillet 1954")
        objet.livre_4 = bl.Livre(4, "Un bonheur insoutenable", "Ira Levin", 9782290332856, "Décembre 1970")

    
    def tester_ajouter_membre(objet):
        print("\nTest (Bibliotheque) - Ajouter un membre")
        #État initial
        objet.assertEqual(len(objet.bibliotheque.membres), 0, "La bibliothèque n'est pas vide au départ")
        #Ajout d'un premier membre
        objet.bibliotheque.ajouter_membre(objet.membre_1)
        objet.assertIn(objet.membre_1, objet.bibliotheque.membres, "Le membre n'a pas été ajouté correctement")
        #Ajout d'un deuxième membre
        objet.bibliotheque.ajouter_membre(objet.membre_2)
        objet.assertIn(objet.membre_2, objet.bibliotheque.membres, "Le membre n'a pas été ajouté correctement")
        #Ajout d'un membre existant
        objet.bibliotheque.ajouter_membre(objet.membre_1)
        objet.assertEqual(objet.bibliotheque.determiner_nombre_membres(), 2, "Il ne reste pas 2 membres dans le système")
    
    
    def tester_supprimer_membre(objet):
        print("\nTest (Bibliotheque) - Supprimer un membre")
        #État initial
        objet.assertEqual(objet.bibliotheque.determiner_nombre_membres(), 0, "La bibliothèque est vide au départ")
        #Ajout de membres (1 et 2)
        objet.bibliotheque.ajouter_membre(objet.membre_1)
        objet.bibliotheque.ajouter_membre(objet.membre_2)
        objet.assertEqual(objet.bibliotheque.determiner_nombre_membres(), 2, "Erreur lors de l'ajout des deux membres")
        #Supprimer un membre
        objet.bibliotheque.supprimer_membre(objet.membre_1)
        objet.assertNotIn(objet.membre_1, objet.bibliotheque.membres, "Erreur lors de la suppression d'un membre")
        #Supprimer le même membre
        objet.bibliotheque.supprimer_membre(objet.membre_1)
        objet.assertEqual(objet.bibliotheque.determiner_nombre_membres(), 1, "Erreur lors de la suppression d'un membre déja supprimé")
        #Supprimer un membre inexistant (3)
        objet.bibliotheque.supprimer_membre(objet.membre_3)
        objet.assertEqual(objet.bibliotheque.determiner_nombre_membres(), 1, "Erreur lors de la suppression d'un membre innexistant")
        #Supprimer le dernier membre
        objet.bibliotheque.supprimer_membre(objet.membre_2)
        objet.assertNotIn(objet.membre_2, objet.bibliotheque.membres, "Erreur lors de la suppression du dernier membre")
        #Supprimer un membre quelconque (liste vide)
        objet.bibliotheque.supprimer_membre(objet.membre_1)
        objet.assertEqual(objet.bibliotheque.determiner_nombre_membres(), 0, "Erreur lors de la suppression d'un membre lors d'une liste vide")


    def tester_ajouter_livre(objet):
        print("\nTest (Bibliotheque) - Ajouter un livre")

        #État initial
        objet.assertEqual(objet.bibliotheque.determiner_grandeur_inventaire(), 0, "La liste de base n'est pas vide")
        #Ajout d'un premier livre
        objet.bibliotheque.ajouter_livre(objet.livre_1)
        objet.assertIn(objet.livre_1, objet.bibliotheque.inventaire_livres, "Le livre n'a pas été ajouté dans l'inventaire")
        #Ajout d'un deuxième livre
        objet.bibliotheque.ajouter_livre(objet.livre_2)
        objet.assertIn(objet.livre_2, objet.bibliotheque.inventaire_livres, "Le livre n'a pas été ajouté dans l'inventaire")
        #Rajouter le même livre
        objet.bibliotheque.ajouter_livre(objet.livre_2)
        objet.assertEqual(objet.bibliotheque.determiner_grandeur_inventaire(), 2, "Le livre à été ajouté malgré sa présence")


    def tester_supprimer_livre(objet):
        
        print("\nTest (Bibliotheque) - Supprimer un livre")
     
        #État initial
        objet.assertEqual(objet.bibliotheque.determiner_grandeur_inventaire(), 0, "L'inventaire n'est pas vide au départ")
        #Ajout de livres (1 et 2)
        objet.bibliotheque.ajouter_livre(objet.livre_1)
        objet.bibliotheque.ajouter_livre(objet.livre_2)
        objet.assertEqual(objet.bibliotheque.determiner_grandeur_inventaire(), 2, "Les deux livres n'ont pas été ajouté")
        #Surpprimer un livre
        objet.bibliotheque.supprimer_livre(objet.livre_1)
        objet.assertNotIn(objet.livre_1, objet.bibliotheque.inventaire_livres, "Le livre est encore dans l'inventaire")
        #Supprimer le même livre
        objet.bibliotheque.supprimer_livre(objet.livre_1)
        objet.assertEqual(objet.bibliotheque.determiner_grandeur_inventaire(), 1, "Erreur lors de la suppression d'un livre déjà supprimé")
        #Supprimer le dernier livre
        objet.bibliotheque.supprimer_livre(objet.livre_2)
        objet.assertNotIn(objet.livre_2, objet.bibliotheque.inventaire_livres, "Erreur lors de la suppression du dernier livre")
     

    def tester_rechercher_par_auteur(objet): #PAS COMPLÉTÉ
        print("\nTest (Bibliotheque) - Rechercher par auteur")
        #État initial
        objet.assertEqual(objet.bibliotheque.determiner_grandeur_inventaire(), 0, "Problème d'initalisation (Nombre de livres incorrect)")

        #Ajout de livres
        objet.bibliotheque.ajouter_livre(objet.livre_1)
        objet.bibliotheque.ajouter_livre(objet.livre_2)
        objet.bibliotheque.ajouter_livre(objet.livre_3)
        objet.bibliotheque.ajouter_livre(objet.livre_4)
        objet.assertEqual(objet.bibliotheque.determiner_grandeur_inventaire(), 4, "Problème d'ajouts (Nombre de livres incorrect)")

        #Recherche par auteur (1 livre)
        nombre_livres_trouves = objet.bibliotheque.rechercher_par_auteur("Ira Levin")

        #Recherche par auteur (2 livres)
       
        #Recherche par auteur (0 livre)
       

    def tester_rechercher_par_titre(objet):  #PAS COMPLÉTÉ
        print("\nTest (Bibliotheque) - Rechercher par titre")
        #État initial
        objet.assertEqual(objet.bibliotheque.determiner_grandeur_inventaire(), 0, "Problème d'initalisation (Nombre de livres incorrect)")

        #Ajout de livres
        objet.bibliotheque.ajouter_livre(objet.livre_1)
        objet.bibliotheque.ajouter_livre(objet.livre_2)
        objet.bibliotheque.ajouter_livre(objet.livre_3)
        objet.bibliotheque.ajouter_livre(objet.livre_4)
        objet.assertEqual(objet.bibliotheque.determiner_grandeur_inventaire(), 4, "Problème d'ajouts (Nombre de livres incorrect)")

        #Recherche par titre (1 livre)
 
        #Recherche par titre (0 livre)
    

if __name__ == "__main__":
    unittest.main()