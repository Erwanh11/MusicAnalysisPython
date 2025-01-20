import pandas as pd
import matplotlib.pyplot as plt


data_path = (
    "data/Spotify-2000.csv"  
)
df = pd.read_csv(data_path)


print("Colonnes disponibles dans le dataset :")
print(df.columns)


if "Year" in df.columns and "Popularity" in df.columns:
    yearly_avg_listens = df.groupby("Year")["Popularity"].mean()
    print("\nNombre moyen d'écoutes par chanson pour chaque année :")
    print(yearly_avg_listens)
else:
    print("\nLes colonnes 'Year' et 'Popularity' sont manquantes dans le dataset.")


plt.figure(figsize=(12, 6))
yearly_avg_listens.plot(kind="line", marker="o", color="teal")
plt.title("Évolution du nombre moyen d'écoutes par année", fontsize=16)
plt.xlabel("Année", fontsize=14)
plt.ylabel("Écoutes moyennes", fontsize=14)
plt.grid(axis="both", linestyle="--", alpha=0.7)


output_path = "visuals/yearly_avg_listens.png"
plt.tight_layout()
plt.savefig(output_path)
plt.show()

print(f"\nGraphique enregistré dans '{output_path}'")


