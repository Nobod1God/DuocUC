import csv 
with open('names.csv', 'r') as a:
    Lector = csv.DictReader(a)
    for linea in Lector:
        nombre = linea['first_name']
        apellido = linea['last_name']
        email = linea['email']
        print(f"{nombre} {apellido} y su email es {email}")