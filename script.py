import pandas as pd

df = pd.read_csv("animes.csv")

df = df.dropna(subset=["Anime", "Note_Globale", "Nb_Episodes"])

df["Note_Globale"] = df["Note_Globale"].astype(float)
df["Nb_Episodes"] = df["Nb_Episodes"].astype(float)

df["popularite"] = df["Nb_Episodes"] / 100
df["score_final"] = 0.6 * df["Note_Globale"] + 0.4 * df["popularite"]

df = df.sort_values(by="score_final", ascending=False)

print("Top 10 des animés :")
for i in range(min(10, len(df))):
    print(i+1, "-", df.iloc[i]["Anime"], "(score :", round(df.iloc[i]["score_final"], 2), ")")
