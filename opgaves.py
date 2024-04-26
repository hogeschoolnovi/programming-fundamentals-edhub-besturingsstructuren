# Opgave 1:
# Schrijf een programma waarbij je twee gehele positieve getallen kunt invoeren. Het programma bepaalt en toont of
# het ene getal een veelvoud is van het andere getal.


getal1 = int(input("voer een getal in: "))
getal2 = int(input("voer een getal in: "))

if getal1 % getal2 == 0:
    print(f"{getal1} is een veelvoud van {getal2}")
elif getal2 % getal1 == 0:
    print(f"{getal2} is een veelvoud van {getal1}")
else:
    print(f"{getal1} en {getal2} zijn geen veelvouden van elkaar")

# Opgave 2:
# De basisprijs van een bioscoopkaartje is 12 euro. Kinderen tot 5 jaar zijn gratis en kinderen van 5 tot 12 jaar betalen de halve prijs. Personen tussen 13 en 54 jaar moeten de volle prijs betalen en vanaf 55 jaar is de toegang weer gratis.
# Maak een programma dat de te betalen prijs afdrukt nadat je de leeftijd hebt ingevoerd.

leeftijd = int(input("voer je leeftijd in: "))
prijs = 12
if leeftijd < 5:
    prijs = 0
elif 5 <= leeftijd < 12:
    prijs = prijs / 2
elif 13 <= leeftijd < 54:
    prijs = prijs
else:
    prijs = 0


print(f"de prijs is: {prijs}")



# Opgave 3:
# Schrijf een programma dat 3 gehele getallen sorteert. De getallen worden ingevoerd en respectievelijk opgeslagen in
# de variabelen num1, num2 en num3. Het programma sorteert de getallen zodanig dat na afloop num1 ≤ num2 ≤ num3.

num1 = int(input("voer een getal in: "))
num2 = int(input("voer een getal in: "))
num3 = int(input("voer een getal in: "))
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1
print(num1, num2, num3)



# Opgave 4: Schrijf een programma dat gehele getallen leest, het totaal en het gemiddelde van deze getallen berekent
# en afdrukt, waarbij 0 niet wordt meegeteld. Het programma eindigt met invoer 0.

totaal = 0
aantal = 0
getal = int(input("voer een getal in: "))
while getal != 0:
    totaal += getal
    aantal += 1
    getal = int(input("voer een getal in: "))
if aantal != 0:
    print(f"totaal: {totaal}")
    print(f"gemiddelde: {totaal / aantal}")
else:
    print("er zijn geen getallen ingevoerd")



# Opgave 5: Schrijf een programma dat de tafel van “factor” afdrukt, nadat je een geheel getal tussen 0 en 10 (de
# “factor”) hebt ingevoerd.
#
# Bijvoorbeeld als factor = 5:
# Out:
#
# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15    # enz.

factor = int(input("voer een getal in: "))
for i in range(1, 11):
    print(f"{i} x {factor} = {i * factor}")

# Opgave 6:
# Schrijf een programma met de volgende functionaliteit:
#
#     Eerst moet je een willekeurig getal invoeren (het “zoekgetal”).
#     Daarna moet je een geheel getal tussen 0 en 10 invoeren (het “aantal”).
#     Tenslotte voer je “aantal” getallen in (dus als aantal = 5 moet je 5 getallen invoeren).
#
# Het programma drukt alle getallen af die kleiner zijn dan het zoekgetal.

zoekgetal = int(input("voer een getal in: "))
aantal = int(input("voer een getal in tussen 0 en 10: "))
if aantal < 0 or aantal > 10:
    print("getal moet tussen 0 en 10 zijn")
else:
    for i in range(aantal):
        getal = int(input("voer een getal in: "))
        if getal < zoekgetal:
            print(getal)

