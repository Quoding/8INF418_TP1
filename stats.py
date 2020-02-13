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
    sex_col = data["sexe"]
    unique, counts = np.unique(sex_col, return_counts=True)
    print(unique, counts)

    # Split selon le sexe
    I_s = data.loc[data["sexe"] == "I"]
    M_s = data.loc[data["sexe"] == "M"]
    F_s = data.loc[data["sexe"] == "F"]
    not_I_s = data.loc[data["sexe"] != "I"]

    # Moyenne de longueur selon le sexe
    print("\n================Moyenne longueur selon sexe================")
    print(I_s.longueur.mean())
    print(M_s.longueur.mean())
    print(F_s.longueur.mean())

    # Ajouter plots de sexe
    # visualisation.make_sex_bar_plot(unique, counts)
    # visualisation.sex_length_height_scatter(I_s, M_s, F_s)
    # visualisation.length_height_scatter(data)

    # Correlation entre hauteur et longueur d'un ormeau
    corr = stats.pearsonr(data.longueur, data.hauteur)

    print(corr)

    print(
        "Hypothese - la longueur  moyenne d'un enfant est significativement differente que la moyenne des F et M"
    )
    # Hypothese - la longueur  moyenne d'un enfant est significativement differente que la moyenne des F et M
    # Nulle --> La longueur moyenne d'un enfant n'est pas significativement differente que celle des adultes
    zscore = (I_s.longueur.mean() - not_I_s.longueur.mean()) / not_I_s.longueur.std()
    p = stats.norm.cdf(zscore)
    print(
        "p-value = " + str(p) + " > 0.05, donc on conserve H nulle"
    )  # p = 0.06944850472833175 -- On ne rejete pas l'hypothese nulle.

    print(
        "Hypothese - le poids moyen d'un enfant est significativement different de la moyenne des F et M"
    )

    # Hypothese - le poids moyen d'un enfant est significativement different que la moyenne des F et M
    # Nulle --> Le poids moyen d'un enfant n'est pas significativement different que celui des adultes
    zscore = (
        I_s.poids_complet.mean() - not_I_s.poids_complet.mean()
    ) / not_I_s.poids_complet.std()
    p = stats.norm.cdf(zscore)
    print(
        "p-value = " + str(p) + " > 0.05, donc on conserve H nulle"
    )  # p = 0.09820540224774799 -- On ne rejete pas l'hypothese nulle.

    # Etude statistique des features p/r au differentes classes
    classes = set(data.nombre_anneau)
    columns = data.columns[1:-1]
    stds = {}
    means = {}

    for column in columns:
        # rendre les dictionnaires nested
        stds[column] = {}
        means[column] = {}
        for classe in classes:
            class_data = data.loc[data["nombre_anneau"] == classe]

            # print("Moyenne de " + column + " pour la classe " + str(classe))
            # print(class_data[column].mean())
            means[column][classe] = class_data[column].mean()

            if len(class_data) > 1:
                # print("Ecart-type de " + column + " pour la classe " + str(classe))
                # print(class_data[column].std())
                stds[column][classe] = class_data[column].std()
            else:
                stds[column][classe] = 0

    # print(stds)
    # print(means)

    visualisation.plot_means_per_attribute_per_class(means)
    visualisation.plot_stds_per_attribute_per_class(stds)


    # Affichage des coefficients de corrélation entre les attributs
    print("\n================Coefficients de corrélation================")

    for attr1 in data.columns[1:9]:
        for attr2 in data.columns[1:9]:
            if attr1 != attr2:
                print(str(attr1) + " et " + str(attr2) + " : " + str(stats.pearsonr(data[attr1], data[attr2])))