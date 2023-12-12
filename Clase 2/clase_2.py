'''
Ejercicio 01
La division de higiene esta trabajando en un control de stock para 
productos sanitarios. Debemos realizar la carga de una compra de productos 
de prevencion de contagio, de cada una debe obtener los siguientes datos:
. El tipo ("barbijo", "jabon" o "alcohol)
. El precio
. La cantidad de unbidasdes
. La marca
. El fabricante

Se debe informar los datos de la compra procesados para poder inicar el control de stock
'''
from os import system
system("cls")


contador_productos = 0
contador_barbijo = 0
contador_jabon = 0
contador_alcohol = 0
contador_mascara = 0

for i in range(5):

    tipo_prodcuto = input("Ingrese producto: 'barbijo', 'jabon', 'mascara' o 'alcohol': ")
    while tipo_prodcuto != "barbijo" and tipo_prodcuto != "jabon" and tipo_prodcuto != "alcohol":
       tipo_prodcuto = input("Error, reingrese producto: ")
    
    precio_producto = float(input("Ingrese precio de producto: "))
    cantidad_unidades = int(input("Ingrese cantidad: "))
    marca_producto = input("Ingrese marca del producto: ")
    fabricante_producto = input("Ingrese el fabricante del producto: ")

    contador_productos += 1

    if tipo_prodcuto == "barbijo":
        contador_barbijo += 1
    elif tipo_prodcuto == "jabon":
        contador_jabon += 1
    elif tipo_prodcuto == "mascara":
        contador_mascara += 1
    else:
        contador_alcohol += 1

    ############################################

    match tipo_prodcuto:
        case "alcohol":
            contador_alcohol +=1
        case "barbijo":
            contador_barbijo += 1
        case "mascara":
            contador_mascara += 1
        case _:
            contador_jabon += 1

     #procesos

    # seguir = input("Desea continuar: ")
    # if seguir != "si":
    #     break

print(f"Se ingresaron: {contador_alcohol} alcoholes")
print(f"Se ingresaron: {contador_jabon} jabones")
print(f"Se ingresaron: {contador_barbijo} barbijos")
print(f"Se ingresaron: {contador_mascara} mascaras")
