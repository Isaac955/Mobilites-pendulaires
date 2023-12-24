import sqlite3
baseDeDonnees=sqlite3.connect('mobilite.db')
curseur =baseDeDonnees.cursor()
baseDeDonnees=sqlite3.connect('mobilite.db')
curseur =baseDeDonnees.cursor()


curseur.execute("SELECT temps_trajet FROM Utilise")
utilise=curseur.fetchall()
curseur.execute("SELECT utilisateurID  FROM Utilise")
utilisateurs=curseur.fetchall()
nombre=max(utilisateurs)
print("Le temps de trajet pour",nombre,"personnes est compris entre ",min(utilise),"et ",max(utilise),"minutes.")


curseur.execute("SELECT commune  FROM utilisateurs WHERE commune = 'Andilly'")
ville=curseur.fetchall()
total=len(ville)
liste_de_caractère="[('Andilly',), ('Eaubonne',), ('Ermont',), ('Le Plessis-Bouchard',), ('Margency',), ('Saint-Prix',), ('Montmorency',), ('Saint-Gratien',), ('Saint-Leu la Forêt',), ('Saint-Prix',), ('Eaubonne',), ('Saint-Leu la Forêt',), ('Eaubonne',), ('Eaubonne',), ('Eaubonne',), ('Saint-Leu la Forêt',), ('Margency',), ('Margency',), ('Eaubonne',), ('Andilly',), ('Andilly',), ('Andilly',), ('Saint-Gratien',), ('Ermont',), ('Ermont',), ('Saint-Gratien',), ('Eaubonne',), ('Eaubonne',), ('Margency',), ('Ermont',)]"
compteur=liste_de_caractère.count('Andilly')
pourcentage=compteur/total*100
print("Le pourcentage de personnes qui habitent à Andilly est de ",pourcentage,"%.")


curseur.execute("SELECT vehiculeID  FROM Utilise WHERE vehiculeID = '6'")
vehicule=curseur.fetchall()
total2=len(vehicule)
liste_de_caractère2="[(2,), (1,), (2,), (4,), (5,), (3,), (6,), (6,), (2,), (3,), (3,), (1,), (1,), (2,), (3,), (4,), (3,), (5,), (5,), (6,), (6,), (1,), (1,), (3,), (3,), (4,), (4,), (2,), (6,), (6,)]"
compteur2=liste_de_caractère2.count('6')
pourcentage2=compteur2/total2*100
print(pourcentage2,"% de personnes vont au lycée à pied." )
