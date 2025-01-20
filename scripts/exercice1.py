import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Charger les données
data_path = "data/Spotify-2000.csv"
df = pd.read_csv(data_path)
print("Aperçu des données :")
print(df.head())

# Afficher les colonnes
print("Valeurs manquantes par colonne :")
print(df.isnull().sum())

# Remplacer les valeurs manquantes
df.fillna({"colonne": "valeur_par_défaut"}, inplace=True)
df.dropna(inplace=True)  

# Afficher les colonnes
print("Statistiques descriptives :")
print(df.describe())
