import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.preprocessing import LabelEncoder
import joblib

data_path = (
    "data/Spotify-2000.csv"  
)
df = pd.read_csv(data_path)

print("Colonnes disponibles dans le dataset :")
print(df.columns)

required_columns = ["Top Genre", "Year", "Popularity"]
if all(col in df.columns for col in required_columns):
    label_encoder = LabelEncoder()
    df["Genre_Encoded"] = label_encoder.fit_transform(df["Top Genre"])

    
    X = df[["Genre_Encoded", "Year"]]
    y = df["Popularity"]

    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
else:
    print("\nLes colonnes nécessaires pour le modèle sont absentes.")
    exit()


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("\nÉvaluation du modèle :")
print(f"R² (coefficient de détermination) : {r2:.4f}")
print(f"MAE (erreur absolue moyenne) : {mae:.2f}")


joblib.dump(model, "models/popularity_prediction_model.pkl")
print("\nModèle sauvegardé dans 'models/popularity_prediction_model.pkl'.")
