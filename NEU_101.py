import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.linear_model import BayesianRidge

# 1. Beispiel-Daten mit fehlenden Werten
df = pd.DataFrame({
    "Alter": [25, 30, np.nan, 45, 50],
    "Einkommen": [3000, np.nan, 3500, 5000, 5200],
    "Arbeitsstunden": [40, 38, 42, np.nan, 45]
})

print("Rohdaten:")
print(df)

# 2. MICE-Imputer definieren
imputer = IterativeImputer(
    estimator=BayesianRidge(),
    max_iter=10,
    random_state=42
)

# 3. Daten imputieren
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print("\nNach MICE-Imputation:")
print(df_imputed)

