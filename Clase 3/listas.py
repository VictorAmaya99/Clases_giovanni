
from os import system
system("cls")
''' 


#Listas

lista = [1,2,3,4,5,6,7,8,9,5,5]
print(lista[3])

acumulador = 0
contador = 0
for i in range(len(lista)):
    acumulador = acumulador + lista[i]
    if lista[i] == 5:
        contador += 1

print(acumulador)
print(contador)

lista.append(100)
lista.append(50)

print(lista)

lista.insert(2,999) #(indice, valor). remplaza el valor en el indice indicado
print(lista)

lista.extend([900,800,777])
print(lista)

lista.remove(5)
print(lista)

print(lista.index(999))

for numero in lista:
    print(numero)

'''
###################################################################

# mi_diccionario = {}

# mi_diccionario["Nombre"] = "Juan"
# mi_diccionario["Edad"] = 25

# print(mi_diccionario)

# otro_diccionario = {"Nombre": "Luis", "Edad": 32}
# print(otro_diccionario)

# for key in otro_diccionario:
#     print(key)

# for key in otro_diccionario:
#     print(f"{otro_diccionario[key]}")

###################################################################

#Listas paralelas:

CANTIDAD_ALUMNOS = 3
# lista_nombres = []
# lista_apellidos = []

# for i in range(CANTIDAD_ALUMNOS):
#     nombre = input("Ingrese nombre: ")
#     apellido = input("Ingrese apellido: ")
#     lista_nombres.append(nombre)
#     lista_apellidos.append(apellido)

# for i in range(CANTIDAD_ALUMNOS):
#     print(f"{i+1})Nombre: {lista_nombres[i]} - Apellido: {lista_apellidos[i]}")

    ###########################################################

    # lista_alumnos = [
    #     {"Nombre": "Juan", "Edad": 25}, 
    #     {"Nombre": "Luis", "Edad": 36}, 
    #     {"Nombre": "Maria", "Edad": 23}
    #     ]
    
lista_alumnos = [
    {'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad': 25}, 
    {'Nombre': 'Luis', 'Apellido': 'Gomez', 'Edad': 64}, 
    {'Nombre': 'Maria', 'Apellido': 'Ruiz', 'Edad': 36}
    ]

# for i in range(CANTIDAD_ALUMNOS):
#     nombre = input("Ingrese nombre: ")
#     apellido = input("Ingrese apellido: ")
#     edad = int(input("Ingrese edad: "))
#     un_alumno = {}
#     un_alumno["Nombre"] = nombre
#     un_alumno["Apellido"] = apellido
#     un_alumno["Edad"] = edad
#     lista_alumnos.append(un_alumno)

# print(lista_alumnos)

# for alumno in lista_alumnos:
#     apellido = alumno["Apellido"]
#     nombre = alumno["Nombre"]
#     edad = alumno["Edad"]
#     if edad > 30:
#          print(f"{apellido}-{nombre}-{edad}")

for alumno in lista_alumnos:
    edad = alumno["Edad"]
    if edad > 30:
         print(f"{alumno['Apellido']}-{alumno['Nombre']}-{alumno['Edad']}")