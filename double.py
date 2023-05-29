#Athor: Copyright © 2023: Tatár Mátyás Bence (https://github.com/tatarmb4s/) - All Right Reserved

# Double feladat

import math
import sys

def gen_dobble_szam(n):
    szamokKartyankent = n
    osszesSzimb = szamokKartyankent**2 - szamokKartyankent + 1 # Mivel számokról van szól, kb végtelen a lehetőség, így le kell valamivel szűkítenem. Ezen dolog miatt a minnél nagyobb számú pakli kijelentés értelmét veszti, mert ha kedvem tartja a végtelenségig generálom őket.
    
    kartyaszam = szamokKartyankent * (szamokKartyankent - 1) + 1

    symbols = list(range(1, osszesSzimb + 1))  # Szimbólumok listája

    csomag_in_gen = []  # Az eredmény számcsomagokat tartalmazó lista

    for i in range(kartyaszam):
        kartya = []  # Egy kártya inicializálása
        for j in range(szamokKartyankent):
            szimbIndex = (i + j * n) % osszesSzimb  # A szimbólum indexének kiszámítása
            kartya.append(symbols[szimbIndex])  # Szimbólum hozzáadása a kártyához
        csomag_in_gen.append(kartya)  # Kártya hozzáadása a számcsomaghoz

    return csomag_in_gen

# Indításnál megadott paraméterek ellenőrzése
if len(sys.argv) < 2:
    print("Hiba: Addj megy egy egyjegyű egész szám paramétert!")
    sys.exit(1)
try:
    # Az n paraméter kiolvasása
    n = int(sys.argv[1])
except:
    print("Hiba: Addj megy egy egyjegyű egész SZÁM paramétert!")
    sys.exit(1)


# Számcsomagok generálása
csomag = gen_dobble_szam(n)

# Kártyák kiíratása
for i, kartya in enumerate(csomag):
    print(f"{i+1}. Kártya: {kartya}")

#Athor: Copyright © 2023: Tatár Mátyás Bence (https://github.com/tatarmb4s/) - All Right Reserved