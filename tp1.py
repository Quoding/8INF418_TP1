import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import stats
import visualisation

# Chargemenet des donnees
data = pd.read_csv(
    "abalone.data",
    names=[
        "sex",
        "length",
        "diameter",
        "height",
        "whole",
        "shucked",
        "viscera",
        "shell",
        "rings",
    ],
)
print("\n================Dataset================")
print(data)
# Statistiques
stats.doStats(data)

# Visualisation
# visualisation.do_class_distrib_barplot(data)
# visualisation.do_sex_class_barplot(data)

