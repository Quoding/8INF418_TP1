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
    not_I_s = data.loc[data["sex"] != "I"]

    # Moyenne de longueur selon le sexe
    print("\n================Moyenne longueur selon sexe================")
    print(I_s.length.mean())
    print(M_s.length.mean())
    print(F_s.length.mean())

    # Ajouter plots de sexe
    # visualisation.make_sex_bar_plot(unique, counts)
    # visualisation.sex_length_height_scatter(I_s, M_s, F_s)
    # visualisation.length_height_scatter(data)

    corr = stats.pearsonr(data.length, data.height)

    print(corr)

    print(
        "Hypothese - la longueur  moyenne d'un enfant est significativement differente que la moyenne des F et M"
    )
    # Hypothese - la longueur  moyenne d'un enfant est significativement differente que la moyenne des F et M
    # Nulle --> La longueur moyenne d'un enfant n'est pas significativement differente que celle des adultes
    zscore = (I_s.length.mean() - not_I_s.length.mean()) / not_I_s.length.std()
    p = stats.norm.cdf(zscore)
    print(
        "p-value = " + str(p) + " > 0.05, donc on conserve H nulle"
    )  # p = 0.06944850472833175 -- On ne rejete pas l'hypothese nulle.

    print(
        "Hypothese - le poids moyen d'un enfant est significativement different de la moyenne des F et M"
    )

    # Hypothese - le poids moyen d'un enfant est significativement different que la moyenne des F et M
    # Nulle --> Le poids moyen d'un enfant n'est pas significativement different que celui des adultes
    zscore = (I_s.whole.mean() - not_I_s.whole.mean()) / not_I_s.whole.std()
    p = stats.norm.cdf(zscore)
    print(
        "p-value = " + str(p) + " > 0.05, donc on conserve H nulle"
    )  # p = 0.09820540224774799 -- On ne rejete pas l'hypothese nulle.

