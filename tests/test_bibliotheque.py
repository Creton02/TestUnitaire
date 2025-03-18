
import gestion_bibliotheque as bl
import unittest


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
  
        #Ajout d'un premier membre
      
        #Ajout d'un deuxième membre
     
        #Ajout d'un membre existant
      
    
    def tester_supprimer_membre(objet):
        print("\nTest (Bibliotheque) - Supprimer un membre")

        #État initial
     
        #Ajout de membres (1 et 2)
    
        #Supprimer un membre
     
        #Supprimer le même membre
       
        #Supprimer un membre inexistant (3)
       
        #Supprimer le dernier membre
     
        #Supprimer un membre quelconque (liste vide)
       

    def tester_ajouter_livre(objet):
        print("\nTest (Bibliotheque) - Ajouter un livre")

        #État initial

        #Ajout d'un premier livre
      
        #Ajout d'un deuxième livre
       
        #Rajouter le même livre
       

    def tester_supprimer_livre(objet):
        
        print("\nTest (Bibliotheque) - Supprimer un livre")
     
        #État initial
     
        #Ajout de livres (1 et 2)
    
        #Surpprimer un livre
      
        #Supprimer le même livre
     
        #Supprimer le dernier livre
     

    def tester_rechercher_par_auteur(objet):
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
       

    def tester_rechercher_par_titre(objet):
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