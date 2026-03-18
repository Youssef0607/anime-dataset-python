import csv

liste_animes = []

with open("animes.csv", "r", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)

    for ligne in lecteur:

        
        if ligne["Anime"] != "" and ligne["Note_Globale"] != "" and ligne["Nb_Episodes"] != "":
            try:
                nom = ligne["Anime"]
                note = float(ligne["Note_Globale"])
                episodes = float(ligne["Nb_Episodes"])

                
                popularite = episodes / 100

                
                score_final = 0.6 * note + 0.4 * popularite

                liste_animes.append([nom, round(score_final, 2)])

            except:
                
                pass


liste_animes.sort(key=lambda x: x[1], reverse=True)


print("Top 10 des animés :")

for i in range(10):
    if i < len(liste_animes):
        print(i+1, "-", liste_animes[i][0], "(score :", liste_animes[i][1], ")")