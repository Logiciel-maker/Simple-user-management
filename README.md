# Simple-user-management
Simplifier la gestion utilisateurs d'une base de donnée en python.
# Objectif :
Se connecter à une base de données SQLite3 en vue de réaliser une gestion simplifiée des utilisateurs. 

#Prérequis : 
 Python 3.7
OS : Windows 10
Module sqlite3 
Module tkinter
Réaliser une connexion Python avec sqlite3 pour générer la base de données.

#Fonctionnement:
L’application a été construite avec tkinter pour fournir à l'utilisateur une interface graphique.
Le programme  stocke des informations telles que le nom complet, l’age, l'addresse et le numéro de téléphone d'un utilisateur.
IL lui permet de visualiser tous les enregistrements d’une table s’il le souhaite en seul coup.
L'utilisateur pourra aussi rechercher une entrée ou en ajouter une autre.
il pourra également mettre à jour une ou supprimer une entrée et pourra  fermer le programme s'il le souhaite, via une interface graphique tkinter.  

Le programme utilise une base de données sqlite3 nommé "database.db". 
Il est fait en deux parties:
fil1 est le script principal, il définit l'interface graphique.
fil2 est le script secondaire, il définit les fonctions auxquelles nous avons fait appel dans le fil1.

#Utilisation:

1-Nous avons prévu  4 champs de saisie où l'utilisateur  pourra entrer un nouvel enregistrement pour la stocker dans la base de données.

2-En suite nous avons conçus des boutons qui permettent à l’utilisateur de réaliser opérations en terme de gestion.
Le Bouton 'Adduser' permet d’enregistrer une saisie
Le Bouton 'Display' permet d’afficher le contenue d’une table.
Le Bouton 'Search' permet d’effectuer une recherche à partir d’une valeur saisie.
Le bouton 'update' permet d’effectuer une mise à jour à partir d’une entrée sélectionnée. 
Le bouton 'Delete' permet de supprimer une entrée sélectionnée.
Le bouton 'Close' ferme l’application.

3-la partie ListBox permet de visualiser les enregistrements.
L’utilisateur pourra aussi  par exemple sélectionner une entrée pour une modification ou pour une suppression.

 
