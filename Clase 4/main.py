from data_stark import lista_personajes
from os import system

system("cls")

'''
1. Mostrar personajes
2. Mostrar personaje con maxima altura
3. Mostrar personaje con minima altura
4. Mostrar suma de la altura
5. Mostrar promedio de la altura
6. Salir

'''

def mostrar_personajes():
    print("Lista de personajes: ")
    for nombre in lista_personajes:
        print(nombre["nombre"])

def mostrar_altura_maxima():
    maximo_altura = 0
    flag_primer_personaje = False

    for personaje in lista_personajes:
        if personaje["altura"] > maximo_altura or flag_primer_personaje == False :
            flag_primer_personaje = True
            maximo_altura = personaje["altura"]

    for personaje in lista_personajes:
        if personaje["altura"] == maximo_altura:
            print(f"El personaje con la altura maxima es: {personaje['nombre']}, con una altura de: {maximo_altura}")

def mostrar_altura_minima():
    minima_altura = 0
    flag_primer_personaje = False

    for personaje in lista_personajes:
        if personaje["altura"] < minima_altura or flag_primer_personaje == False:
            flag_primer_personaje = True
            minima_altura = personaje["altura"]

    for personaje in lista_personajes:
        if personaje["altura"] == minima_altura:
            print(f"El personaje con la altura minima es: {personaje['nombre']}, con una altura de: {minima_altura}")

def mostrar_suma_altura():
    acumulador_altura = 0

    for personaje in lista_personajes:
        acumulador_altura += personaje["altura"]

    print(f"la suma de la altura de los personajes es: {acumulador_altura:.2f}")

def mostrar_promedio_altura():
    acumulador_altura = 0
    contador_altura = 0

    for personaje in lista_personajes:
        acumulador_altura += personaje["altura"]
        contador_altura += 1

    promedio_altura = acumulador_altura / contador_altura
    print(f"El promedio de la altura de los personajes es: {promedio_altura:.2f}")

system("cls")
while True:
    respuesta = int(input("""
    1. Mostrar personajes
    2. Mostrar personaje con maxima altura
    3. Mostrar personaje con minima altura
    4. Mostrar suma de la altura
    5. Mostrar promedio de la altura
    6. Salir
    Elija una opcion:  """))
    match respuesta:
        case 1:
            mostrar_personajes()            
        case 2:
            mostrar_altura_maxima()
        case 3:
            mostrar_altura_minima()
            
        case 4:
            mostrar_suma_altura()
        case 5:
           mostrar_promedio_altura()

        case 6:
            break 

