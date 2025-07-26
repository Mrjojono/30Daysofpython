import math

age = 18
taille = 1.68

numero_complex = 2j

##calcule d ezone d'un triangle
base = int(input("entrer la  base:"))
hauteur = int(input("entrer la hauteur:"))

print(f"la zone du triangle est de: {0.5 * base * hauteur}")

##calcule du perimetre du triangle
A = int(input("entrer le coté A:"))
B = int(input("entrer le coté B:"))
C = int(input("entrer le coté C:"))

print(f"le périmetre du traingle est  {A + B + C}")

longueur = int(input("entrer la longueur de votre rectangle:"))
largeur = int(input("entrer la largeur de votre rectangle"))

surface = longueur * largeur
perimetre = 2 * (longueur + largeur)
print(f"surface du rectangle est {surface} et perimetre est {perimetre}")

rayon = int(input("entrer le rayon du cercle"))
pi = 3.14
print(f"zone du cercle est {pi * rayon * rayon} \n la circonference est {2 * pi * rayon}")


## donnons une valeur quelconque a X
def f(x):
    return 2 * x - 2


# Calcul des points
x1 = 0
y1 = f(x1)

x2 = 1
y2 = f(x2)

m = (y2 - y1) / (x2 - x1)

print(f"la pente est de {m}")

A1 = (2, 2)
A2 = (6, 10)
m2 = (A2[1] - A1[1]) / (A2[0] - A1[0])
l = pow((A2[0] - A1[0]), 2) + pow((A2[1] - A1[1]), 2)
print(f"la pente entre {A1} et {A2} est: {m2} et la distance eucleudienne est {math.sqrt(l)}  ")

if m < m2:
    print("m est inferieur m2")
elif m > m2:
    print("m est superieur a m2")
elif m == m2:
    print("m est egale a  m2")

x = [1, 3, 6, 7, 5, -3]

found = False
for i in x:
    y = i ** 2 + 6 * i + 9
    if y == 0:
        print(f"La valeur de x pour laquelle y est égale à 0 est {i}")
        found = True
if not found:
    print("Aucune valeur de x ne donne y = 0")

mot1 = "Python"
mot2 = "Dragon"

print("Les longueurs sont différentes ? ", len(mot1) != len(mot2))

if "on" in mot1 and "on" in mot2:
    print("on se trouve dans le deux mots")
else:
    print("on ne se trouve pas dans les deux mots")

prase = "14. I hope this course is not full of jargon."

if "jargon" in prase:
    print("jargon se trouve dans la phrase")


if "on" not in mot1 and "on " not in mot2:
    print("on ne se trouve dans aucun des mots")
else:
    print("on se trouve dans les deux mots")

long = len(mot1)

print(f"longeur de python en flotteur {float(long)} longeur en chaine {str(long)}");



print(f"2 est pair sit {8%2} = 0")

l = 7//3

if l == int(2.7):
    print(" la division de plancher de 7 par 3 est egale a Int(2.7)")
else:
    print("les deux valeur ne sont pas egale")

r = 10
if type("«10»") == type(r):
    print("«10» et 10 on un type egale")
else:
    print("ils on un type differents")

if int('9.8') == 10 :
    print('int(9.8) est egale a 10')
else:
    print('int(9.8) est differents  de 10')

heure = int(input("entrer les heures:"))
taux = int(input("entrer le taux par heure"))

print(f"votre gain hebdomadaire est {taux*heure}")

exit()
