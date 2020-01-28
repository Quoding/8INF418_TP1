import numpy
import pandas as pd

# Voici un equivalent du pretraitement fait au dataset si le dataset n'avais pas deja ete pretraite
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

data = data.dropna(how="any")
data[["length", "diameter", "height", "whole", "shucked", "viscera", "shell"]] /= 200

print(data)

