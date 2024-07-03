nombres = []
apellidos = []
while len(nombres) < 3:
    entrada = input("Ingrese un nombre para anadir a la lista. Maximo 3: ")
    nombres.append(entrada)
    anadir = input("desea anadir otro nombre a la lista? s/n  ")
    if anadir == "s":
        continue
    else:
        break
while len(apellidos) < 3:
    entrada2 = input("Ingrese un apellido. Maximo 3: ")
    apellidos.append(entrada2)
   
    
print(nombres, apellidos)

