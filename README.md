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

## Résultat 
Top 10 des animés :
  
- 1 - One Piece (score : 9.58 )
- 2 - Naruto Shippuden (score : 6.92 )
- 3 - Dragon Ball Z (score : 6.38 )
- 4 - Bleach (score : 6.2 )
- 5 - Hunter x Hunter (2011) (score : 5.99 )
- 6 - Naruto (score : 5.92 )
- 7 - Fullmetal Alchemist: Brotherhood (score : 5.72 )
- 8 - Haikyuu!! (score : 5.56 )
- 9 - Steins;Gate (score : 5.56 )
- 10 - L'Attaque des Titans (score : 5.46 )

Auteur : Myriam Youssef
