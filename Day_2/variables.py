first_name = " iron "
last_name = " joan"
full_name = first_name + last_name
country = "TOGO"
city = "Lomé"
age = 17
year = 2026
is_married = False
is_true = True
is_light_on = False

a, b, c = 1, 2, 3

# Affichage des types
print(f"type de first_name : {type(first_name)}")
print(f"type de last_name : {type(last_name)}")
print(f"type de full_name : {type(full_name)}")
print(f"type de country : {type(country)}")
print(f"type de city : {type(city)}")
print(f"type de age : {type(age)}")
print(f"type de year : {type(year)}")
print(f"type de is_married : {type(is_married)}")
print(f"type de is_true : {type(is_true)}")
print(f"type de is_light_on : {type(is_light_on)}")
print(f"type de a : {type(a)}")
print(f"type de b : {type(b)}")
print(f"type de c : {type(c)}")

print(f"lenth de first name {len(first_name)}")
print(f"lenth de last name {len(last_name)}")

if len(first_name) < len(last_name):
    print("longueur de first_name < last_name")
elif len(first_name) > len(last_name):
    print("longueur de first_name > last_name")
elif len(first_name) == len(last_name):
    print("longueur de first_name = last_name")

num_one = 5
num_two = 4

total_add =  num_one + num_two
print(f"addition de {num_one} et {num_two} = {total_add}")
total_sous = num_one - num_two
print(f"soustration de {num_one} et {num_two} = {total_sous}")
total_multi =  num_one * num_two
print(f"multiplication de {num_one} et {num_two} = {total_multi}")
total_div = num_one /  num_two
print(f"division de {num_one} par {num_two} =  {total_div}")
total_modulo = num_two % num_one
print(f"modulo de {num_two } par {num_one} = {total_modulo}")
total_power = pow(num_one,num_two)
print(f"puissance de {num_one} a {num_two} = {total_power}")
floor_division = num_one//num_two
print(f"floor division de {num_one} par {num_two} =  {floor_division} ")

raduis = 30

print(f"aire du cercle de rayon {raduis} est  {3.14*pow(raduis,2)}")
print(f"circonference du cercle de rayon {raduis} est  {3.14*2*raduis}")

user_input_raduis = input("entrer l'air du cercle ")
print(f"aire du cercle de rayon {user_input_raduis} est  {3.14*pow(user_input_raduis,2)}")

first_name_input = input("enter first_name")
last_name_input = input("enter last_name")
country_input = input("enter country")
age = input("enter age")

