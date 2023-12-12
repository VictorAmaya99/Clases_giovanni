# 4-
# Debemos desarrollar un algoritmo que permita computar los votos del Senado de
# Berlinberlín. Se deberá ingresar el nombre de cada senador y si está Presente o no en
# la sesión. Si el senador está presente, se deberá pedir el valor del voto
# El voto de los senadores berliberlineses puede ser Afirmativo, Negativo o Abstención
# (validar). El valor por defecto para los senadores ausentes será Abstención.
# Se deberá Informar:

# o Cantidad total de senadores.
# o Cantidad de senadores presentes.
# o Cantidad y porcentaje de votos afirmativos.
# o Cantidad y porcentaje de votos negativos.
# o Cantidad y porcentaje de abstenciones.
# o Generar una lista de senadores por cada tipo de voto y mostrarlas por
# pantalla.

from os import system
system("cls")

seguir = "si"
cantidad_senadores = 0
cantidad_sen_presentes = 0
cantidad_total_votos = 0
cantidad_votos_afirmativos = 0
cantidad_votos_negativos = 0
cantidad_abstenciones = 0
lista_afirmativos = []
lista_negativos = []
lista_abstenciones = []

while seguir == "si":
    
    nombre_senador = input("Ingrese nombre del senador: ")
    presentismo = input("Ingresar si el senador esta presente, si o no:  ")
    while presentismo != "si" and presentismo != "no":
        presentismo = input("Error, reingresar presentismo: ")
    valor_voto = input("Ingrese valor del voto: afirmativo, negativo, abstencion: ")
    while valor_voto != "afirmativo" and valor_voto != "negativo" and valor_voto != "abstencion":
        valor_voto = input("Error, reingresar valor del voto: ")

# o Cantidad total de senadores.
    cantidad_senadores = cantidad_senadores + 1
    if presentismo == "si":
        cantidad_sen_presentes = cantidad_sen_presentes + 1
    
    
        
    match valor_voto:
        case "afirmativo":
            lista_afirmativos.append(nombre_senador)
            cantidad_votos_afirmativos += 1
        case "negativo":
            lista_negativos.append(nombre_senador)
            cantidad_votos_negativos += 1
        case "abstencion":
            lista_abstenciones.append(nombre_senador)
            cantidad_abstenciones += 1
    
    cantidad_total_votos += 1
    seguir = input("Desea continuar:")


porcentaje_votos_afirmativos = cantidad_votos_afirmativos / cantidad_total_votos * 100
porcentaje_votos_negativos = cantidad_votos_negativos / cantidad_total_votos * 100
porcentaje_abstenciones = cantidad_abstenciones / cantidad_total_votos * 100

print(f"La cantidad total de senadores es: {cantidad_senadores}")
print("------------------------------------------------------------")
print(f"La cantidad de senadores presentes es: {cantidad_sen_presentes}")
print("------------------------------------------------------------")
print(f"la cantidad de votos afirmativos es: {cantidad_votos_afirmativos} y el porcentaje es : {porcentaje_votos_afirmativos}")
print("------------------------------------------------------------")
print(f"la cantidad de votos negativos es: {cantidad_votos_negativos} y el porcentaje es : {porcentaje_votos_negativos}")
print("------------------------------------------------------------")
print(f"la cantidad de abstenciones es: {cantidad_abstenciones} y el porcentaje es : {porcentaje_abstenciones}")
print("------------------------------------------------------------")
print(f"los senadores que votaron 'si' fueron: {lista_afirmativos}")
print("------------------------------------------------------------")
print(f"los senadores que votaron 'no' fueron: {lista_negativos}")
print("------------------------------------------------------------")
print(f"los senadores que se abstuvieron fueron: {lista_abstenciones}")

