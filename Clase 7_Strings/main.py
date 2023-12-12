from data_stark import lista_personajes
from funciones import *
from os import system

'''
[
    {
        'title': 'QUEVEDO || BZRP Music Sessions #52',
        'views': 227192970,
        'length': 204,
        'img_url': 'http://i.ytimg.com/vi/A_g3lMcWV0/sddefault.jpg',
        'url': 'http://youtube.com/watch?v=A_g3lMcWVy0',
        'date': '2022-07-06 00:00:00'
    } 
] 

Tipo : BZRP Music Sessions
Artista : QUEVEDO
Numero : 52
Reproducciones : 227 M
Duracion : 204 segundos
Codigo : A_g3lMcWVy0
Fecha de carga : 6/7/2022
Hora de carga : 00:00

'''
# def prueba(): #parser
#     titulo = 'QUEVEDO || BZRP Music Sessions #52'
#     parte1 = titulo.split("||")
#     artista = parte1[0].strip()
#     parte2 = parte1[1].split("#")
#     tipo = parte2[0].strip()
#     tipo = tipo.upper()
#     numero = parte2[1]
    
#     print(f"out: {artista}-{numero}-{tipo}")

# def prueba1(titulo:str):
#     titulo = 'QUEVEDO || BZRP Music Sessions #52'
#     parte1 = titulo.split("||")
#     artista = parte1[0].strip()
#     parte2 = parte1[1].split("#")
#     tipo = parte2[0].strip()
#     tipo = tipo.upper()
#     numero = parte2[1]
    
#     print(f"out: {artista}-{numero}-{tipo}")



def calcular_maximo(lista:list, clave:str)->int: 
    maximo = 0
    flag_primer_personaje = False

    if(type(lista) == list and len(lista) > 0 and type(clave) == str):
        for personaje in lista :
            if personaje[clave] > maximo or flag_primer_personaje == False :
                flag_primer_personaje = True
                maximo = personaje[clave]
    return maximo

def mostrar_altura_maxima(lista:list):
    maximo_altura = calcular_maximo(lista, 'altura')
    
    if(maximo_altura != 0):
        print("El personja con maxima altura es: ")
        mostrar_personajes(lista, 'altura', maximo_altura)
    else:
        print("Ocurrio un error")

def mostrar_peso_maximo(lista:list):
    maximo_peso = calcular_maximo(lista, 'peso')
    
    print("Personaje con maximo peso: ")
    mostrar_personajes(lista, 'peso', maximo_peso)


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
    6. Mostrar personaje mazimo peso
    7. Salir
    Elija una opcion:  """))
    match respuesta:
        case 1:
            mostrar_personajes(lista_personajes)            
        case 2:
            mostrar_altura_maxima(lista_personajes)
        case 3:
            #mostrar_altura_minima()
            pass
        case 4:
            mostrar_suma_altura()
        case 5:
           mostrar_promedio_altura()
        case 6:
            mostrar_peso_maximo(lista_personajes)

        case 7:
            break 

