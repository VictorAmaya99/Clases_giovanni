'''
En la gala final de Gran Hermano y la produccion nos pide un 
programa para contar los votos de los televidentes y saber cual
será el participante que ganará el juego.

Los participantes finalistas son: Nacho, Julieta y Marcos.

El televidente debe ingresar:
. Nombre del vontante(debe ser mayor a 13)
. Genero del votante (masculino, femenino)
. El nombre del participante a quien le dara el voto positivo.

No se sabe cuántos votos entrarán durante la gala

Se debe informar al usurario:

A. El promedio de edad de los votantes de genero femenino.
B. Cantidad de personas de genero masculino entre 25 y 40 años votaron a Nacho o Julieta.
C. Nombre del votante mas joven que voto a Nacho.
D. Nombre de cada participante y porcentaje de votos que recibio.
E. El nombre del participante que gano el reality (El que tiene mas votos)
'''

from os import system
system("cls")

seguir = "si"
cantidad_votantes_nacho_0_julieta = 0
acumulador_edad_femenino = 0
contador_edad_femenino = 0
flag_mas_joven = False
edad_mas_joven = None
nombre_mas_joven = None
acumulador_votos_nacho = 0
acumulador_votos_julieta = 0
acumulador_votos_marcos = 0
contador_votos_nacho = 0
contador_votos_julieta = 0
contador_votos_marcos = 0
contador_total_votos = 0
acumulador_total_votos = 0
participante_mas_votos = None


while seguir == "si":
    nombre_votante = input("Ingrese nombre: ")
    
    edad_votante = int(input("Ingrese edad: "))
    while edad_votante < 13:
        edad_votante = int(input("Error, reingrese edad: "))

    genero_votante = input("Ingrese genero: 'masculino' o 'femenino': ")
    while genero_votante != "masculino" and genero_votante != "femenino":
        genero_votante = input("Error reingrese genero: ")

    nombre_participante = input("Nombre del participante a votar: 'nacho', 'julieta' o 'marcos': ")
    while nombre_participante != "nacho" and nombre_participante != "julieta" and nombre_participante != "marcos":
        nombre_participante = input("Error, reingrese nombre del participante: ")

    #B. Cantidad de personas de genero masculino entre 25 y 40 años votaron a Nacho o Julieta.
    if genero_votante == "masculino" and edad_votante >= 25 and edad_votante <= 45 and nombre_participante == "nacho" or nombre_participante == "julieta":
        cantidad_votantes_nacho_0_julieta += 1

    #C. Nombre del votante mas joven que voto a Nacho.
    if flag_mas_joven == False and nombre_participante == "nacho":
        flag_mas_joven = True
        edad_mas_joven = edad_votante
        nombre_mas_joven = nombre_votante
    else:
        nombre_mas_joven = nombre_votante

    #D. Nombre de cada participante y porcentaje de votos que recibio.
    match nombre_participante:
        case "nacho":
            acumulador_votos_nacho += 1
            contador_votos_nacho += 1
        
        case "julieta":
            acumulador_votos_julieta += 1
            contador_votos_julieta += 1
        
        case "marcos":
            acumulador_votos_marcos += 1
            contador_votos_marcos += 1
    
        
    acumulador_edad_femenino = edad_votante
    contador_edad_femenino += 1
    acumulador_total_votos += 1
    contador_total_votos += 1

    seguir = input("Desea continuar: ")

#A. El promedio de edad de los votantes de genero femenino.
promedio_edad_votantes_femenino = acumulador_edad_femenino / contador_edad_femenino

porcentaje_votos_nacho = acumulador_votos_nacho / acumulador_total_votos * 100
porcentaje_votos_julieta = acumulador_votos_julieta / acumulador_total_votos * 100
porcentaje_votos_marcos = acumulador_votos_marcos / acumulador_total_votos * 100

#E. El nombre del participante que gano el reality (El que tiene mas votos)
if contador_votos_nacho > contador_votos_julieta and contador_votos_nacho > contador_votos_marcos:
    participante_mas_votos = "nacho"
elif contador_votos_marcos > contador_votos_julieta:
    participante_mas_votos = "marcos"
else:
    participante_mas_votos = "julieta"

print(cantidad_votantes_nacho_0_julieta)
print(promedio_edad_votantes_femenino)
print(f"La edad del vontante mas joven que voto a Nacho fue {edad_mas_joven} y su nombre es {nombre_mas_joven}")
print(f"el porcentaje de votos de nacho fue: {porcentaje_votos_nacho}")
print(f"el porcentaje de votos de julieta fue: {porcentaje_votos_julieta}")
print(f"el porcentaje de votos de marcos fue: {porcentaje_votos_marcos}")


print(f"El ganador del concurso es: {participante_mas_votos}")
