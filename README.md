# Mobilité pendulaires
Le but de ce projet était d'étudier les mobilités pendulaires (déplacement domicile-travail) de tous les acteurs du Lycée Louis Armand à Eaubonne (élèves, enseignants et personnels).


# 1. Conception du formulaire
- Création un formulaire en HTML du Lycée Louis Armand (à Eaubonne) pour collecter les données nécessaires : commune de résidence, statut (élève, enseignant, personnel) & moyen de transport utilisé.
- CSS pour styliser le formulaire et le rendre + convivial.
- JavaScript pour valider les entrées utilisateur et améliorer l'expérience utilisateur.

# 2. Création de la base de données
- Utilisation de la library SQLite3 de Python pour créer la base de données
- Création d'une table pour stocker les réponses au formulaire (commune de résidence, statut, moyen de transport).
- Programmation des scripts Python pour importer les résultats du formulaire dans la base de données depuis des fichiers CSV

# 3. Analyse des résultats
- Programmation des scripts Python pour extraire et analyser les données de la base de données SQLite3.
- Calculez la proportion de mobilités douces en fonction des réponses au formulaire.
- Analysez si l'usage est conditionné par la commune de résidence en effectuant des requêtes SQL appropriées.
