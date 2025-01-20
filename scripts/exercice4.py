import pandas as pd
from tabulate import tabulate


data_path = "data/Spotify-2000.csv"
df = pd.read_csv(data_path)


print("Colonnes disponibles dans le dataset :")
print(df.columns)


if "Popularity" in df.columns:
    global_mean_listens = df["Popularity"].mean()
    print(f"\nMoyenne globale des écoutes : {global_mean_listens:.2f}")
else:
    print("\nLa colonne 'Popularity' est absente du dataset.")


if "Popularity" in df.columns:
    popular_songs = df[df["Popularity"] > global_mean_listens].sort_values(
        by="Popularity", ascending=False
    )
    print(
        f"\nNombre de chansons ayant un nombre d'écoutes supérieur à la moyenne : {len(popular_songs)}"
    )
else:
    popular_songs = pd.DataFrame()


if not popular_songs.empty:
    top_10_songs = popular_songs[["Title", "Artist", "Popularity"]].head(10)
    print("\nTop 10 des chansons les plus populaires :")
    print(
        tabulate(top_10_songs, headers="keys", tablefmt="fancy_grid", showindex=False)
    )
else:
    print("\nAucune chanson ne dépasse la moyenne globale des écoutes.")


output_path = "data/top_10_songs.csv"
if not popular_songs.empty:
    top_10_songs.to_csv(output_path, index=False)
    print(
        f"\nLe tableau des 10 meilleures chansons a été sauvegardé dans '{output_path}'."
    )
