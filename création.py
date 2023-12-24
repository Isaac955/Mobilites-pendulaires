
#Importation de la bibliothèque sqlite3
import sqlite3

#Création et/ou connection à la base de données
baseDeDonnees = sqlite3.connect('mobilite.db')

#Création d'un curseur sur la connexion
curseur = baseDeDonnees.cursor()

#Exécution d'une requête SQL de création de table
curseur.execute("""CREATE TABLE Utilise
                 (vehiculeID INT,
                  utilisateurID INT,
                  temps_trajet INT,
                  piste_cyclables INT,
                  FOREIGN KEY (vehiculeID) REFERENCES Vehicules(vehiculeID),
                  FOREIGN KEY (utilisateurID) REFERENCES Utilisateurs(utilisateurID)
                  );
                  """)
curseur.execute("""CREATE TABLE Connaissance
                 (utilisateurID INT,
                   raisonID INT,
                   commentaire TEXT ,
                   FOREIGN KEY (utilisateurID) REFERENCES Utilisateurs(utilisateurID),
                   FOREIGN KEY (raisonID) REFERENCES Raisons(raisonID)
                 );""")
curseur.execute("""CREATE TABLE Vehicules
                 (vehiculeID INT NOT NULL,
                  vehicule_desc TEXT,
                  PRIMARY KEY (vehiculeID));""")

curseur.execute("""CREATE TABLE Utilisateurs
                 (utilisateurID INT,
                 nom TEXT NOT NULL,
                 prenom TEXT NOT NULL,
                 categorie TEXT ,
                 commune TEXT,
                 num_rue INT,
                 nom_rue TEXT,
                 PRIMARY KEY (utilisateurID));""")

curseur.execute("""CREATE TABLE Mesures
                 (mesureID INT,
                  mesure_desc TEXT,
                  PRIMARY KEY (mesureID));""")
curseur.execute("""CREATE TABLE Raisons
                 (raisonID INT,
                  raison_desc TEXT,
                  PRIMARY KEY (raisonID));""")

curseur.execute("""CREATE TABLE Incitation
                 (mesureID INT,
                  utilisateurID INT,
                  FOREIGN KEY (mesureID) REFERENCES Mesures(mesureID),
                 FOREIGN KEY (utilisateurID) REFERENCES Utilisateurs(utilisateurID));""")


# On envoie la requête SQL
baseDeDonnees.commit()


baseDeDonnees.commit()

baseDeDonnees.close()