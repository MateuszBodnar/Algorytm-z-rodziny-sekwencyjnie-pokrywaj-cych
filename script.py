from itertools import combinations, product

def generuj_reguly_rzedu(df, rzad):

    atrybuty = df.columns[:-1]
    reguly = []

    for combo in combinations(atrybuty, rzad):

        wartosci = [df[a].unique() for a in combo]

        for values in product(*wartosci):

            warunki = list(zip(combo, values))

            podzbior = df.copy()

            for a, v in warunki:
                podzbior = podzbior[podzbior[a] == v]

            if len(podzbior) == 0:
                continue

            decyzje = podzbior['d'].unique()

            if len(decyzje) == 1:

                reguly.append((warunki, decyzje[0], list(podzbior.index)))

    return reguly
