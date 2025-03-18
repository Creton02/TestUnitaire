import gestion_bibliotheque as bl
import unittest


class TestLivre(unittest.TestCase):

    def setUp(objet):
        objet.livre_test_valide = bl.Livre(1, "Dune", "Frank Herbert", 9780441172719, "Août 1965")
        objet.livre_test_invalide = bl.Livre(23, "Python pour les nuls", "John-Paul Mueller", 9782412028872, "Aoû 2023")
    
 
    def tester_afficher_valide(objet):
        print("\nTest (Livre) - Affichage valide")
        objet.assertEqual(objet.livre_test_valide.afficher_description(), "[1] - Dune (Août 1965) Auteur(e) : Frank Herbert [Disponible : OUI]", "L'objet n'a pas été créé avec les bonnes informations")

   
    # test : tester_afficher_invalide

if __name__ == "__main__":
    unittest.main()