# 3-
# Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición
# de memoria es la que mas ocurrencias tiene dentro de esa lista.
from os import system
system("cls")

lista_numeros = []




for i in range(10):
    numeros = int(input("Ingrese numeros: "))
    lista_numeros.append(numeros)
    #lista_numeros.count(numeros)
print(f"el numero {[2]}, tiene un total de {lista_numeros.count(2)}")

#print("el numero con mas ocurrencias es: ", lista_numeros.count(2))


