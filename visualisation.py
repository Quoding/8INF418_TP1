import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np


def do_class_distrib_barplot(data):
    grp_cnt = data.groupby(["rings"])[
        "rings"
    ].count()  # Cree une liste qui contient la distribution pour chaque classe

    grp_cnt.plot.bar()
    plt.ylabel("Nombre d'instances")
    plt.xlabel("Nombre d'anneau (Classe)")

    plt.show()
