chaine1 = "trente" + " " + "jours" + " " + "de" + " " + "python"
print("1:", chaine1)

chaine2 = "codage" + " " + "pour" + " " + "all"
print("2:", chaine2)

societe = "codage pour tous"
print("4:", societe)
print("5:", len(societe))

print("6:", societe.upper())


print("7:", societe.lower())


texte = "Coding For All"
print("8.1:", texte.capitalize())
print("8.2:", texte.title())
print("8.3:", texte.swapcase())


print("9:", texte[7:])

print("10:", "Coding" in texte)

print("11:", societe.replace("codage", "Python"))
texte2 = "Python pour tout le monde"
print("12:", texte2.replace("tout le monde", "tous"))

print("13:", societe.split())


entreprises = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("14:", entreprises.split(", "))

print("15:", texte[0])


print("16:", texte[-1])


chaine3 = "codage pour toutes"
print("17:", chaine3[10])


phrase1 = "Python pour tout le monde"
acronyme1 = "".join([mot[0].upper() for mot in phrase1.split()])
print("18:", acronyme1)


phrase2 = "codage pour tous"
acronyme2 = "".join([mot[0].upper() for mot in phrase2.split()])
print("19:", acronyme2)

texte = "codage pour tous"
texte2 = "codage de toutes les personnes"


print("20:", texte.find('C'))
print("20 (en minuscule c):", texte.find('c'))

chaine = "Coding For All"
print("21:", chaine.find('F'))
print("22:", texte2.rfind('l'))

phrase = "Vous ne pouvez pas mettre fin à une phrase avec parce que parce que c'est une conjonction"


print("23:", phrase.find("parce que"))


print("24:", phrase.rindex("parce que"))


start = phrase.find("parce que")
end = phrase.find("c'est")
print("25:", phrase[start:end].strip())


print("26:", phrase.find("parce que"))


start = phrase.find("parce que")
second_parce_que = phrase.find("parce que", start + 1)
print("27:", phrase[start:second_parce_que + len("parce que")].strip())

chaine1 = "Coding For All"
print("28:", chaine1.startswith("Coding"))


chaine2 = "Codage pour tous"
print("29:", chaine2.endswith("coding"))


chaine3 = "  Codage pour tous  "
print("30:", chaine3.strip())


var1 = "30daysofpython"
var2 = "Thirty_days_of_python"
print("31 var1:", var1.isidentifier())
print("31 var2:", var2.isidentifier())

frameworks = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
joined_string = ' # '.join(frameworks)
print("32:", joined_string)

print("33:\nJ'apprécie ce défi.\nJe me demande juste quelle est la prochaine étape.")

print("34:\nName\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10
pi = 3.14
area = pi * radius ** 2
print("35:\nLa zone d'un cercle avec le rayon {} est de {:.0f} mètres carrés.".format(radius, area))

a = 8
b = 6


print("36:\n{} + {} = {}".format(a, b, a + b))


print("Copyright © {} Skill Foundry".format(2025))


print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))
