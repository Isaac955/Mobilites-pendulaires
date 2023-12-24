import sqlite3
import csv
file = open('vehicule.csv','r')
vehicule= csv.DictReader(file, delimiter=',')

file2 = open('utilisateurs.csv','r')
utilisateur= csv.DictReader(file2, delimiter=',')

file3 = open('utilise.csv','r')
utilise= csv.DictReader(file3, delimiter=',')

file4 = open('raisons.csv','r')
raisons= csv.DictReader(file4, delimiter=',')

file5 = open('connaissance.csv','r')
connaissance= csv.DictReader(file5, delimiter=',')

file6 = open('mesures.csv','r')
mesures= csv.DictReader(file6, delimiter=',')

file7 = open('incitation.csv','r')
incitation= csv.DictReader(file7, delimiter=',')

baseDeDonnees = sqlite3.connect('mobilite.db')
curseur = baseDeDonnees.cursor()

for mobilite in vehicule:
    # On ajoute un enregistrement depuis un dictionnaire
 	curseur.execute("INSERT INTO Vehicules (vehiculeID, vehicule_desc) VALUES (:vehiculeID, :vehicule_desc);", mobilite)
baseDeDonnees.commit()
idDernierEnregistrement = curseur.lastrowid # Récupère l'ID de la dernière ligne insérée.
baseDeDonnees.close()

for mobilite in utilisateur:
    # On ajoute un enregistrement depuis un dictionnaire
 	curseur.execute("INSERT INTO Utilisateurs (utilisateurID, nom, prenom,categorie,commune,num_rue,nom_rue) VALUES (:utilisateurID, :nom, :prenom, :categorie, :commune, :num_rue, :nom_rue);", mobilite)
baseDeDonnees.commit()
idDernierEnregistrement = curseur.lastrowid # Récupère l'ID de la dernière ligne insérée.
baseDeDonnees.close()


for mobilite in utilise:
    # On ajoute un enregistrement depuis un dictionnaire
 	curseur.execute("INSERT INTO Utilise (utilisateurID, vehiculeID, temps_trajet, piste_cyclables) VALUES (:utilisateurID, :vehiculeID, :temps_trajet, :piste_cyclables);", mobilite)
baseDeDonnees.commit()
idDernierEnregistrement = curseur.lastrowid # Récupère l'ID de la dernière ligne insérée.
baseDeDonnees.close()

for mobilite in raisons:
    # On ajoute un enregistrement depuis un dictionnaire
 	curseur.execute("INSERT INTO Raisons (raisonID,raison_desc) VALUES (:raisonID, :raison_desc);", mobilite)
baseDeDonnees.commit()
idDernierEnregistrement = curseur.lastrowid # Récupère l'ID de la dernière ligne insérée.
baseDeDonnees.close()

for mobilite in mesures:
    # On ajoute un enregistrement depuis un dictionnaire
 	curseur.execute("INSERT INTO Mesures (mesureID,mesure_desc) VALUES (:mesureID, :mesure_desc);", mobilite)
baseDeDonnees.commit()
idDernierEnregistrement = curseur.lastrowid # Récupère l'ID de la dernière ligne insérée.
baseDeDonnees.close()

for mobilite in incitation:
    # On ajoute un enregistrement depuis un dictionnaire
 	curseur.execute("INSERT INTO Incitation (utilisateurID,mesureID) VALUES (:utilisateurID, :mesureID);", mobilite)
baseDeDonnees.commit()
idDernierEnregistrement = curseur.lastrowid # Récupère l'ID de la dernière ligne insérée.
baseDeDonnees.close()

