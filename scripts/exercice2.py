import pandas as pd
import matplotlib.pyplot as plt

data_path = (
    "data/Spotify-2000.csv"  
)
df = pd.read_csv(data_path)

# Vérifier les colonnes disponibles
print("Colonnes disponibles dans le dataset :")
print(df.columns)

# Compter le nombre de chansons par genre dans tout le dataset
genre_counts = df["Top Genre"].value_counts()
print("\nNombre total de chansons par genre :")
print(genre_counts)

# Identification genre le plus représenté dans le top 100
# Trier le dataset par Popularité pour obtenir le top 100
top_100 = df.nlargest(100, "Popularity")

# Compter les genres dans le top 100
top_100_genre_counts = top_100["Top Genre"].value_counts()
print("\nNombre de chansons par genre dans le Top 100 :")
print(top_100_genre_counts)

# Identification genre dominant dans le Top 100
most_common_genre_top_100 = top_100_genre_counts.idxmax()
most_common_count_top_100 = top_100_genre_counts.max()
print(
    f"\nLe genre le plus représenté dans le Top 100 est '{most_common_genre_top_100}' avec {most_common_count_top_100} chansons."
)

# graphique pour la répartition des genres dans le Top 100
plt.figure(figsize=(12, 6))
top_100_genre_counts.plot(kind="bar", color="lightgreen")
plt.title("Répartition des genres dans le Top 100", fontsize=16)
plt.xlabel("Genre musical", fontsize=14)
plt.ylabel("Nombre de chansons", fontsize=14)
plt.xticks(rotation=45, ha="right", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)


output_path = "visuals/top_100_genre_distribution.png"
plt.tight_layout()
plt.savefig(output_path)
plt.show()

print(f"\nGraphique enregistré dans '{output_path}'")
