import pandas as pd
from itertools import combinations, product

data = {
    'a1': [1, 1, 1, 1, 1, 1, 1, 1],
    'a2': [1, 1, 1, 1, 1, 1, 1, 1],
    'a3': [1, 1, 1, 1, 2, 2, 2, 2],
    'a4': [1, 1, 3, 3, 1, 1, 2, 2],
    'a5': [3, 3, 2, 3, 2, 2, 3, 4],
    'a6': [1, 2, 1, 2, 1, 2, 1, 1],
    'd':  [1, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)
df.index = ['o1','o2','o3','o4','o5','o6','o7','o8']

print(df)

def znajdz_pokrycie(df, warunki):

    podzbior = df.copy()

    for attr, val in warunki:
        podzbior = podzbior[podzbior[attr] == val]

    if len(podzbior) == 0:
        return None

    decyzje = podzbior['d'].unique()

    if len(decyzje) == 1:
        return decyzje[0], list(podzbior.index)

    return None

def covering_algorithm(df):

        atrybuty = list(df.columns[:-1])

        aktywne = list(df.index)

        reguly = []

        rzad = 1

        while aktywne and rzad <= len(atrybuty):

            print(f"\nRząd {rzad}:")

            znaleziono_w_rzedzie = False

            for obiekt in aktywne[:]:

                wiersz = df.loc[obiekt]

                znaleziono = False

                for combo_attr in combinations(atrybuty, rzad):

                    warunki = [(attr, wiersz[attr]) for attr in combo_attr]

                    podzbior = df.copy()

                    for attr, val in warunki:
                        podzbior = podzbior[podzbior[attr] == val]

                    if len(podzbior) == 0:
                        continue

                    decyzje = podzbior["d"].unique()

                    # niesprzeczna reguła
                    if len(decyzje) == 1:

                        decyzja = decyzje[0]
                        pokryte = list(podzbior.index)

                        warunki_txt = " ∧ ".join(
                            [f"({a} = {v})" for a, v in warunki]
                        )

                        print(
                            f"z {obiekt} {warunki_txt} ⇒ (d = {decyzja}) [{len(pokryte)}]"
                        )

                        print(
                            f"wyrzucamy z rozważań obiekty: {', '.join(pokryte)}"
                        )

                        reguly.append(
                            (rzad, obiekt, warunki, decyzja, pokryte)
                        )

                        # usuwamy tylko z listy aktywnych
                        for p in pokryte:
                            if p in aktywne:
                                aktywne.remove(p)

                        znaleziono = True
                        znaleziono_w_rzedzie = True
                        break

                if not znaleziono:
                    print(f"z {obiekt} brak")

            rzad += 1

        return reguly

reguly = covering_algorithm(df)
