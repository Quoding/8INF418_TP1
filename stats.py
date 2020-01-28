def doStats(data):
    # Overview des donnees recoltees avec la moyenne, l'ecart-type, les quartiles et le max
    print("\n================Describe================")
    print(data.describe())
    print("\n================Minimums================")
    print(data.iloc[:, 1:].min())
