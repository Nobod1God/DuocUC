def validar_lista_numeros(lista):
   try:
      return [int(numero) for numero in lista]
   except ValueError:
      return None
   
lista_numeros = input("Ingrese una lista de numeros sepadados por espacios: ")
num = validar_lista_numeros(lista_numeros)
lista_par = []
lista_impar = [] 
for numero in lista_numeros:
   if numero % 2 == 0:
      lista_par.append(numero)
   else:
      lista_impar.append(numero)

      