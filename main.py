nume_fisier = input("\nIntrodu numele fișierului text (cu extensia): ")

try:
    with open(nume_fisier, 'r') as f:
        continut = f.read()
        sir_fisier = [float(x) for x in continut.split()]
        print("Șirul citit din fișier este:", sir_fisier)
except FileNotFoundError:
    print(f"Eroare: Fișierul '{nume_fisier}' nu există!")
