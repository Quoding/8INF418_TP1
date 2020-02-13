import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from decimal import Decimal


def do_class_distrib_barplot(data):
    grp_cnt = data.groupby(["rings"])[
        "rings"
    ].count()  # Cree une liste qui contient la distribution pour chaque classe

    grp_cnt.plot.bar()
    plt.title("Distribution des classes")
    plt.ylabel("Nombre d'instances")
    plt.xlabel("Nombre d'anneau (Classe)")

    plt.show()


# Methode de visualisation non vue en classe. C'est un bar plot, mais a plusieurs paliers (i.e. stats par sexe par classe)
# Tu nous avais confirme que c'etait correct.
def do_sex_class_barplot(data):
    # data to plot
    n_groups = 29

    # Extrait le nombre d'observation par sexe par classe
    I_s = data.loc[data["sex"] == "I"].groupby(["rings"], as_index=True)["sex"].count()
    M_s = data.loc[data["sex"] == "M"].groupby(["rings"], as_index=True)["sex"].count()
    F_s = data.loc[data["sex"] == "F"].groupby(["rings"], as_index=True)["sex"].count()

    # print(I_s)
    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 1
    opacity = 0.8

    rects1 = plt.bar(
        I_s.index, I_s.values, bar_width / 3, alpha=opacity, color="g", label="I"
    )
    rects2 = plt.bar(
        M_s.index + (bar_width / 3),
        M_s.values,
        bar_width / 3,
        alpha=opacity,
        color="b",
        label="M",
    )
    rects3 = plt.bar(
        F_s.index + (2 * (bar_width / 3)),
        F_s.values,
        bar_width / 3,
        alpha=opacity,
        color="r",
        label="F",
    )

    plt.xlabel("Sexe par classe")
    plt.ylabel("Nombre d'observations")
    plt.title("Distribution du nombre d'observation par sexe par classe")
    plt.xticks(index + bar_width)
    plt.legend()

    plt.tight_layout()
    plt.show()


def make_sex_bar_plot(unique, counts):
    plt.bar(unique, counts)
    plt.title("Distribution des sexes")
    plt.xlabel("Sexe")
    plt.ylabel("Nombre d'observations")
    plt.show()


def sex_length_height_scatter(I_s, M_s, F_s):
    alpha = 1

    I_s.plot.scatter(
        alpha=alpha, x="longueur", y="hauteur", subplots=True, c="green", label="I"
    )
    plt.title("Hauteur en fonction de la longueur")
    plt.xlabel("Longueur (mm)")
    plt.ylabel("Hauteur (mm)")

    M_s.plot.scatter(
        alpha=alpha, x="longueur", y="hauteur", subplots=True, c="blue", label="M"
    )
    plt.title("Hauteur en fonction de la longueur")
    plt.xlabel("Longueur (mm)")
    plt.ylabel("Hauteur (mm)")

    F_s.plot.scatter(
        alpha=alpha, x="longueur", y="hauteur", subplots=True, c="red", label="F"
    )
    plt.title("Hauteur en fonction de la longueur")
    plt.xlabel("Longueur (mm)")
    plt.ylabel("Hauteur (mm)")

    plt.legend()

    plt.show()


def length_height_scatter(data):
    data.plot.scatter(x="longueur", y="hauteur")
    plt.title("Hauteur en fonction de la longueur")
    plt.xlabel("Longueur (mm)")
    plt.ylabel("Hauteur (mm)")
    plt.show()


def plot_means_per_attribute_per_class(means):
    for feature in means:
        # print(feature)
        plt.bar(list(means[feature].keys()), list(means[feature].values()))
        plt.xlabel("Classes (nombre d'anneaux)")
        plt.ylabel(feature)
        plt.title("Moyenne de " + feature + " selon la classe")
        plt.show()


def plot_stds_per_attribute_per_class(stds):
    for feature in stds:
        # print(feature)
        plt.bar(list(stds[feature].keys()), list(stds[feature].values()))
        plt.xlabel("Classes (nombre d'anneaux)")
        plt.ylabel(feature)
        plt.title("Ecart-type de " + feature + " selon la classe")
        plt.show()
