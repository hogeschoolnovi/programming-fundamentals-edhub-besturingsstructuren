# ==========================================
# Voorbeeld Opdracht
# Gegeven zijn de variabelen a = 3 en b = 10. Evalueer met een if statement of a groter is dan b. Als dat zo is, print dan a. Als dat niet zo is, print dan b.
# ==========================================

a = 3
b = 10

if a > b:
    print(a)
else:
    print(b)

# ==========================================
# Opgave 1:
# Gegeven is een int input geatal1 en getal2 en drie print methodes. Schrijf een if statement dat controleert of getal1 een veelvoud is van getal2, andersom of dat beide getallen geen veelvoud zijn van de ander.
# Zet de juiste print methode op de goede plek in je if statement.
# Voorbeeld goede output: 10 is een veelvoud van 5
# ==========================================


getal1 = int(input("voer een getal in: "))
getal2 = int(input("voer een getal in: "))

if getal1 % getal2 == 0:
    print(f"{getal1} is een veelvoud van {getal2}")
elif getal2 % getal1 == 0:
    print(f"{getal2} is een veelvoud van {getal1}")
else:
    print(f"{getal1} en {getal2} zijn geen veelvouden van elkaar")


# ==========================================
# Opgave 2:
# De basisprijs van een bioscoopkaartje is 12 euro.

# - Kinderen tot 5 jaar zijn gratis
# - kinderen van 5 tot 12 jaar betalen de halve prijs.
# - Personen tussen 13 en 54 jaar moeten de volle prijs betalen
# - vanaf 55 jaar is de toegang weer gratis.

# Maak een programma dat de te betalen prijs afdrukt nadat je de leeftijd hebt ingevoerd als input.
# Voorbeeld output: Voor de leeftijd 10 jaar is de prijs: 6.0
# ==========================================

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


print(f"Voor de leeftijd {leeftijd} jaar is de prijs: {prijs}")



# ==========================================
# Opgave 3:
# Schrijf een programma dat 3 gehele getallen (integers) sorteert. De willekeurige inputs worden opgeslagen in de variabelen num1, num2 en num3. Schrijf een if statement die het laagste getal in num1 stopt, het middelste getal in num2 en het hoogste getal in num3.

# Print de variabelen in de volgorde num1, num2, num3.
# Voorbeeld input: 3 1 2
# Voorbeeld output: 1 2 3
# ==========================================

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



# ==========================================
# Opgave 4:
# Gegeven is de variabele 'totaal' met een waarde van 0. Schrijf een programma dat herhaaldelijk een getal als input vraagt. Elk getal dat je invoert moet moet worden opgeteld bij het totaal. Als je 0 invoert moet het programma stoppen en met een print statement het totaal en het gemiddelde van de getallen afdrukken. Als er geen getallen zijn ingevoerd moet het programma afdrukken: "er zijn geen getallen ingevoerd".

# Voorbeeld input: 2, 4, 6, 0
# Voorbeeld output: totaal: 12, gemiddelde: 4.0
# ==========================================

totaal = 0
aantal_te_printen_getallen = 0

getal = int(input("voer een getal in: "))
# Zo lang er geen 0 wordt ingevoerd blijft de while loop doorgaan
while getal != 0:
    totaal += getal  # Het ingevoerde getal wordt bij het totaal opgeteld
    aantal_te_printen_getallen += 1  # Elke loop verhoogt het aantal_te_printen_getallen met 1
    getal = int(input("voer een getal in: "))
# Pas als er een 0 wordt ingevoerd wordt de loop gestopt en het totaal en het gemiddelde geprint
if aantal_te_printen_getallen != 0:
    print(f"totaal: {totaal}")
    print(f"gemiddelde: {totaal / aantal_te_printen_getallen}")
else:
    print("er zijn geen getallen ingevoerd")



# ==========================================
# Opgave 5:
# Schrijf een input die een integer verwacht en stop deze in de variabele “factor”.
# Schrijf daarna een programma dat de tafel van “factor” afdrukt, Print de tafel van 'factor' van 1 tot en met 10.

# Voorbeeld input: 5
# Voorbeeld output:
#   1 x 5 = 5
#   2 x 5 = 10
#   3 x 5 = 15    # enz. tot en met 10
# ==========================================

factor = int(input("voer een getal in: "))
for i in range(1, 11):
    print(f"{i} x {factor} = {i * factor}")





