# Exercice 3 : Analyse des Résultats

## Biais Potentiel dû à la Taille du Dataset
Les données de ce dataset couvrent une période étendue (1956-2019) avec un échantillon restreint pour les premières années. Cela pourrait introduire un biais significatif dans les moyennes, surtout pour les années où peu de chansons sont représentées. Par exemple :
- **1956** : Cette année ne contient qu'une poignée de chansons populaires. La moyenne reflète donc seulement quelques titres, limitant sa représentativité.
- **2018-2019** : Les années récentes disposent probablement de davantage de données, rendant les moyennes plus robustes.

## Années Clés dans l’Histoire de la Musique
### Années 1960-1961
Une forte augmentation des écoutes coïncide avec :
- L’émergence du **rock and roll**.
- La popularité croissante des artistes tels qu’**Elvis Presley**.
- L’évolution technologique (radio, disques vinyles), qui a contribué à une plus large diffusion musicale.

### Années 2017-2019
Le pic en **2019** pourrait être attribué à :
- La montée des plateformes de streaming comme **Spotify** et **Apple Music**, facilitant l’accès à la musique.
- Les artistes dominants de cette période, tels qu’**Ed Sheeran**, **Drake**, et **Taylor Swift**, avec des albums à succès mondial.

## Fluctuations Inattendues en 2018
La baisse en **2018** est intrigante. Elle pourrait s’expliquer par :
- Un nombre élevé de titres avec des scores de popularité relativement bas.
- Une saturation du marché et une fragmentation des goûts musicaux.

## Conclusion
Bien que des tendances globales soient perceptibles, il est crucial de noter que ce dataset ne représente qu'une fraction de la musique produite chaque année. Des analyses supplémentaires intégrant des données externes (ventes, streams) et des contextes historiques pourraient affiner les conclusions.

---

# Exercice 6 : Analyse Critique des Performances du Modèle

## Résultats du Modèle
- **R² (Coefficient de détermination)** : 0.0328  
  Ce score très faible montre que le modèle explique seulement **3,28 %** de la variance des données. Les variables utilisées (année et genre musical) sont insuffisantes pour prédire efficacement la popularité d'une chanson.
- **MAE (Erreur absolue moyenne)** : 11.57  
  Une erreur moyenne de **11,57** indique une différence notable entre les prédictions et les valeurs réelles, reflétant une faible précision du modèle.

## Limites et Observations
1. **Manque de Variables Explicatives**  
   Les variables disponibles (année et genre) ne capturent pas les facteurs complexes qui influencent la popularité musicale, comme :
   - Les préférences des auditeurs.
   - Les campagnes marketing.
   - Les tendances sociales.

2. **Impact des Genres Musicaux**  
   L'encodage numérique des genres (**LabelEncoder**) simplifie excessivement les relations complexes entre les différents styles musicaux. Par exemple :
   - Des genres similaires comme le **pop** et le **rock** peuvent avoir des influences distinctes sur la popularité.

3. **Biais des Données**  
   Le dataset semble se concentrer uniquement sur les chansons populaires, excluant les morceaux moins écoutés. Cela réduit la diversité des exemples et limite les informations exploitables.

## Conclusion
Avec un **R² de 0.0328** et un **MAE de 11.57**, le modèle actuel a des performances faibles, illustrant que les variables utilisées n'expliquent qu'une petite partie de la popularité des chansons. Des améliorations significatives sont nécessaires pour obtenir des prédictions plus précises.

# Projet : Analyse de la Popularité Musicale

Ce projet explore les tendances de la popularité musicale en utilisant un dataset contenant des informations sur les chansons de 1956 à 2019. Chaque exercice se concentre sur une analyse ou un modèle spécifique pour mieux comprendre les données ou prédire la popularité des chansons.

---

## Structure des Fichiers

- `exercice1.py` : Analyse des colonnes disponibles et exploration initiale des données.
- `exercice2.py` : Visualisation des moyennes annuelles de popularité.
- `exercice3.py` : Analyse des résultats avec une perspective critique sur les tendances.
- `exercice4.py` : Préparation des données pour une modélisation simple.
- `exercice5.py` : Implémentation d'un modèle de régression linéaire pour prédire la popularité.


---

## Instructions pour Utiliser le Projet

### Pré-requis
1. **Environnement Python** : Assurez-vous d'avoir Python 3.7 ou supérieur installé.
2. **Bibliothèques nécessaires** :
   - pandas
   - matplotlib
   - scikit-learn
   - joblib
   - tabulate

Installez-les avec la commande suivante si nécessaire :
```bash
pip install pandas matplotlib scikit-learn joblib tabulate

Structure des Dossiers :
data/Spotify-2000.csv : Dataset utilisé.
models/ : Contiendra le modèle sauvegardé après l'exécution de l'exercice 5.
visuals/ : Contiendra les graphiques générés.