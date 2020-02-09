import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import stats
import visualisation

# Chargemenet des donnees
data = pd.read_csv(
    "abalone.data",
    names=[
        "sexe",
        "longueur",
        "diametre",
        "hauteur",
        "poids_complet",
        "poids_viande",
        "poids_visceres",
        "poids_coquille",
        "nombre_anneau",
    ],
)
print("\n================Dataset================")
print(data)
# Statistiques
stats.doStats(data)

# Visualisation
# visualisation.do_class_distrib_barplot(data)
# visualisation.do_sex_class_barplot(data)

