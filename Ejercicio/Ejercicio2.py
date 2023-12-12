# 2-
# La real academia española nos pide desarrollar un pequeño programa que contenta el
# diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
# algoritmo que nos permita el ingreso de una palabra en español y su traducción al
# ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
# palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
# esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
# debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
# inglés. Recordar validar los datos de forma correcta.

from os import system
system("cls")

lista_español = []
lista_ingles = []
seguir = "si"

while seguir == "si":
    palabra_español = input("Ingrese palabra en español: ")
    if palabra_español not in lista_español:
        lista_español.append(palabra_español)
        palabra_ingles = input("Ingrese traduccion: ")
        lista_ingles.append(palabra_ingles)
    else:
        print(f"la palabra {palabra_español} ya se encuentra en la lista, en el indice: {lista_español.index(palabra_español)}")
              

                

    seguir = input("Desea continuar: ")
        
for i in range(len(lista_español)):
    print(f"{i+1})Español: {lista_español[i]} - Traduccion al ingles: {lista_ingles[i]}")
        



    



# while seguir == "si":
#     palabra_español = input("Ingrese palabra en español: ")
#     palabra_ingles = input("Ingrese traduccion: ")
#     lista_español.append(palabra_español)
#     lista_ingles.append(palabra_ingles)

    
#     seguir = input("Desea continuar: ")



# for i in range(len(lista_español)):
#     print(f"{i+1})Español: {lista_español[i]} - Traduccion al ingles: {lista_ingles[i]}")
    


