# ---------------------------------------
# 📦 Importation des librairies
# ---------------------------------------

import pandas as pd          # Manipulation et analyse de données (DataFrame)
import numpy as np           # Calcul scientifique, opérations sur tableaux numériques
import matplotlib.pyplot as plt  # Création de graphiques (courbes, histogrammes…)
import seaborn as sns        # Visualisations avancées et plus jolies (basé sur matplotlib)

from sklearn.model_selection import train_test_split  
# Sépare le dataset en données d'entraînement et de test

from sklearn.preprocessing import StandardScaler  
# Normalisation des données : moyenne = 0 et écart-type = 1

from sklearn.linear_model import LinearRegression  
# Modèle de régression linéaire (prédire une variable continue)

from sklearn.ensemble import RandomForestRegressor  
# Modèle puissant d’ensemble d’arbres de décision (prédiction non linéaire)

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error  
# Mesures de performance des modèles de régression (erreurs + R²)

import warnings
warnings.filterwarnings('ignore')  
# Ignore les warnings pour garder l’affichage propre


# ---------------------------------------
# ⚙️ Configuration générale
# ---------------------------------------

np.random.seed(42)  
# Assure la reproductibilité des opérations aléatoires (split, modèles, etc.)

plt.style.use('seaborn-v0_8-darkgrid')  
# Style de graphique avec quadrillage sombre (plus esthétique)

sns.set_palette("husl")  
# Palette de couleurs harmonieuses pour seaborn


print("✓ Toutes les librairies sont importées avec succès!")
