# Citirea șirului de numere de la tastatură
intrare_sir = input("Introdu numerele separate prin spațiu: ")
sir = [float(x) for x in intrare_sir.split()]
print("Șirul este:", sir)

# Citirea matricei de la tastatură
linii = int(input("Introdu numărul de linii: "))
coloane = int(input("Introdu numărul de coloane: "))

matrice = []
print(f"Introdu elementele pentru fiecare linie ({linii}x{coloane}):")
for i in range(linii):
    linie_input = input(f"Linia {i + 1}: ")
    elemente = [float(x) for x in linie_input.split()]
    matrice.append(elemente)

print("Matricea este:")
for linie in matrice:
    print(linie)

