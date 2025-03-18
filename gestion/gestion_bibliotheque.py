"""
Votre nom
Laboratoire 07 - Gestion d'une bibliothèque
"""

import re

class Livre:
     def __init__(objet, id, titre, auteur, ISBN, date_parution):
          #Initalisation des attributs reçus en paramètres
          objet.id = id
          objet.titre = titre
          objet.auteur = auteur
          objet.ISBN = ISBN
          objet.date_parution = date_parution
          ## Si la date ne respecte pas le format suivant (Mois XXXX), elle est automatique remplacée par la date (Janvier 2000)
          regex = r"^[A-Za-zéèêëîïôöûüÉÈÊËÎÏÔÖÛÜ]+ \d{4}$"
          if re.match(regex, objet.date_parution):
               pass
          else:
               objet.date_parution = "Janvier 2000"
          objet.est_emprunte = False
          objet.emprunteur = -1


     def afficher_description(objet):
          """
          Cette fonction doit retourner une variable de texte (str) sous le format suivant :
          [id] - Nom (Date de parution) Auteur(e) : Nom de l'auteur [Disponible : OUI/NON]
          Si le livre est emprunté (True) -> NON
          Si le livre n'est pas emprunté (False) -> OUI
          """
          retour = ""
          retour += f"[{objet.id}] - "
          retour += f"{objet.titre} ({objet.date_parution}) "
          retour += f"Auteur(e) : {objet.auteur} "
          est_disponible = "OUI"
          if objet.est_emprunte == True:
               est_disponible = "NON"
          retour += f"[Disponiple : {est_disponible}]"
          
          return (retour)

        
class Membre:
    def __init__(objet, nom, id):
          objet.nom = nom
          objet.id = id
          objet.livres_empruntes = []

    def emprunter_livre(objet, livre:Livre):
          liste_id = faire_liste_identifiants(objet.livres_empruntes)
          if livre.id not in liste_id:
               print(f"Emprunt du livre suivant : {livre.afficher_description()}")
               livre.est_emprunte = True
               livre.emprunteur = objet.id
               objet.livres_empruntes.append(livre)
          else:
               print(f"Vous avez déjà emprunté ce livre : {livre.afficher_description()}")

    def rapporter_livre(objet, livre:Livre):
          liste_id = faire_liste_identifiants(objet.livres_empruntes)
          if livre.id in liste_id:
               print(f"Retour du livre suivant : {livre.afficher_description()}")
               objet.livres_empruntes.remove(livre)
               livre.est_emprunte = False
               livre.emprunteur = -1
          else:
              print(f"Vous n'avez pas emprunté ce livre : {livre.afficher_description()}")

    def determiner_nombre_livres_empruntes(objet):
         return len(objet.livres_empruntes)
    
    def __str__(objet):
         return f"[{objet.id}] - {objet.nom}"


class Bibliotheque:
     def __init__(objet):
          objet.inventaire_livres = []
          objet.membres = []
     
     def ajouter_membre(objet, membre:Membre):
          liste_id = faire_liste_identifiants(objet.membres)

          if membre.id not in liste_id:
               objet.membres.append(membre)
               print(f"Ajout du membre suivant : {membre}")
          else:
               print("Il existe déjà un membre avec cet identifiant")
          

     def supprimer_membre(objet, membre:Membre):
          liste_id = faire_liste_identifiants(objet.membres)
          if membre.id in liste_id:
               objet.membres.remove(membre)
               print(f"Suppression du membre suivant : {membre}")
          else:
               print("Aucun membre avec cet identifiant")


     def ajouter_livre(objet, livre:Livre):
          liste_id = faire_liste_identifiants(objet.inventaire_livres)
          if livre.id not in liste_id:
               objet.inventaire_livres.append(livre)
               print(f"Le livre No {livre.id} a été ajouté dans l'inventaire.")
          else:
               print(f"Le livre No {livre.id} est déja dans l'inventaire.")
          objet.inventaire_livres
          """
          Cette fonction doit ajouter un livre dans l'inventaire

          Si le l'id du livre n'est pas dans la liste d'id
               On le rajoute et on affiche un message approprié
          Sinon
               On affiche un message approprié       
          """
     

     def supprimer_livre(objet, livre:Livre):
          liste_id = faire_liste_identifiants(objet.inventaire_livres)
          if livre.id in liste_id:
               objet.inventaire_livres.remove(livre)
               print(f"Le livre No {livre.id} a été supprimé de l'inventaire.")
          else:
               print(f"Le livre No {livre.id} n'était pas dans l'inventaire, il ne peut être supprimé.")
          """
          Cette fonction doit supprimer un livre de l'inventaire

          Si le l'id du livre est dans la liste d'id
               On le supprime et on affiche un message approprié
          Sinon
               On affiche un message approprié       
          """


     def determiner_grandeur_inventaire(objet):
          return len(objet.inventaire_livres)


     def determiner_nombre_membres(objet):
          return len(objet.membres)
     

     def rechercher_par_auteur(objet, nom_auteur:str):
          """
          Cette fonction doit retourner une liste des livres qui respecte le critère de nom
          Pour tous les livres de l'inventaire de la bibliothèque
               Si le nom de l'auteur est égal au nom du l'auteur du livre actuel
                    On ajoute ce livre          
          """
          retour = []
          for livre in range(len(objet.inventaire_livres)):
               if objet.inventaire_livres[livre] == nom_auteur:
                    retour.append(objet.inventaire_livres[livre])
          return retour
     
     
     def rechercher_par_titre(objet, titre:str):
          """
          Cette fonction doit retourner une liste des livres qui respecte le critère de titre

          Pour tous les livres de l'inventaire de la bibliothèque
               Si le titre reçu est contenu (in) dans le titre du livre actuel
                    On ajoute ce livre          
          """
          retour = []
          for livre in range(len(objet.inventaire_livres)):
               if objet.inventaire_livres[livre].titre == titre:
                    retour.append(objet.inventaire_livre[livre])
          return retour

def faire_liste_identifiants(liste_a_analyser):
     liste_id = []
     for element_actuel in liste_a_analyser:
          liste_id.append(element_actuel.id)
     return liste_id
