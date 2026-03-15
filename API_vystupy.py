from vstupy import *

pridej_zamestnance(1, "Jan Novak")
pridej_zamestnance(2, "Petr Svoboda")
prirad_kartu_zamestnanci("KARTA123", 1)
prirad_kartu_zamestnanci("KARTA456", 2)

zaznamenej_prichod("KARTA123")
zaznamenej_prichod("KARTA456")
zaznamenej_prichod("KARTA456")  # Petr Svoboda odchází

print("Záznamy pro KARTA123:")
for zaznam in ziskej_zaznamy(kod="KARTA123"):
    print(zaznam)

print("Záznamy pro zaměstnance 2:")
for zaznam in ziskej_zaznamy(cislo=2):
    print(zaznam)

print("Kdo je přítomen?")
print(f"Přítomen je {kdo_je_pritomen()}")
