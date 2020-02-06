from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import visualisation


def doStats(data):
    # Overview des donnees recoltees avec la moyenne, l'ecart-type, les quartiles et le max
    print("\n================Describe================")
    print(data.describe())
    print("\n================Minimums================")
    print(data.iloc[:, 1:].min())

    # Distribution des sexes
    print("\n================Sex distribution================")
    sex_col = data["sex"]
    unique, counts = np.unique(sex_col, return_counts=True)
    print(unique, counts)

    # Split selon le sexe
    I_s = data.loc[data["sex"] == "I"]
    M_s = data.loc[data["sex"] == "M"]
    F_s = data.loc[data["sex"] == "F"]

    # Moyenne de longueur selon le sexe
    print("\n================Moyenne longueur selon sexe================")
    print(I_s.length.mean())
    print(M_s.length.mean())
    print(F_s.length.mean())

    # Ajouter plots de sexe
    # visualisation.make_sex_bar_plot(unique, counts)
    # visualisation.sex_length_height_scatter(I_s, M_s, F_s)
    visualisation.length_height_scatter(data)
    corr = stats.pearsonr(data.length, data.height)
    print(corr)
