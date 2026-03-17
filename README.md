# anime-dataset-python
# Analyse d'un dataset d'animés

## Objectif
Ce projet Python a pour but de :

- Charger un dataset d'animés (`animes.csv`)
- Nettoyer les données et gérer les valeurs manquantes
- Calculer un score simple pour chaque animé
- Produire un classement du Top 10 des animés

## Contenu du projet
- `animes.csv` : fichier dataset
- `anime_script.py` : script Python qui analyse les données

## Méthodologie
- Le score final est calculé ainsi :  
  `score_final = 0.6 * Note_Globale + 0.4 * Popularité`  
- La popularité est basée sur le nombre d'épisodes

Auteur : Myriam Youssef
