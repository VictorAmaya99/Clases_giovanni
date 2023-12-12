# Ejercicios Listas
# 1-
# Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
# autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
# marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
# mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
# listas primero, y despues usando listas y comparar la composición del código.

from os import system
system("cls")

lista_marca_auto = []
lista_año_auto = []
lista_precio_auto = []

seguir = "si"

while seguir == "si":

    marca_auto = input("Ingrese marca del auto: ")
    año_auto = input("Ingrese año del auto: ")
    precio_auto = float(input("Ingrese precio del auto: "))
    lista_marca_auto.append(marca_auto)
    lista_año_auto.append(año_auto)
    lista_precio_auto.append(precio_auto)



    seguir = input("Desea continuar: ")



for i in range(len(lista_marca_auto)):
    print(f"{i+1})Marca: {lista_marca_auto[i]} - Año: {lista_año_auto[i]} - Precio: {lista_precio_auto[i]}")

