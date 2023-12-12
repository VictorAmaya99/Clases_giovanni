
### Recorrer la lista imprimiendo los nombres de los heroes
# for nombre in lista_personajes:
#     print(nombre["nombre"])

###Recorrer la lista imprimiendo por consola el nombre de cada heroe
###junto a la identidad de cada uno

# for personaje in lista_personajes:
#     print(f"{personaje['nombre']} - {personaje['identidad']}")

### Recorrer la lista para saber cual es la altura maxima

maximo_altura = 0
flag_primer_personaje = False

for personaje in lista_personajes:
    if personaje["altura"] > maximo_altura or flag_primer_personaje == False :
        flag_primer_personaje = True
        maximo_altura = personaje["altura"]

print(f"La maxima altura es: {maximo_altura}")

### Recorrer la lista para saber cual es la altura minima

minima_altura = 0
flag_primer_personaje = False

for personaje in lista_personajes:
    if personaje["altura"] < minima_altura or flag_primer_personaje == False:
        flag_primer_personaje = True
        minima_altura = personaje["altura"]

print(f"La minima altura es: {minima_altura}")

### Recorrer la lista y determinar el total de altura de personajes
acumulador_altura = 0

for personaje in lista_personajes:
    acumulador_altura += personaje["altura"]

print(f"la suma de la altura de los personajes es: {acumulador_altura:.2f}")

### Recorrer la lista y determinar el promedio de la altura de los personajes
acumulador_altura = 0
contador_altura = 0

for personaje in lista_personajes:
    acumulador_altura += personaje["altura"]
    contador_altura += 1

promedio_altura = acumulador_altura / contador_altura

print(f"El promedio de la altura de los personajes es: {promedio_altura:.2f}")

### Informar cual el nombre del personaje asociado a cada uno de los indicadores
### anteriores (Maximo, Minimo, Acumulador y promedio)

maximo_altura = 0
flag_primer_personaje = False

for personaje in lista_personajes:
    if personaje["altura"] > maximo_altura or flag_primer_personaje == False :
        flag_primer_personaje = True
        maximo_altura = personaje["altura"]

for personaje in lista_personajes:
    if personaje["altura"] == maximo_altura:
        print(personaje["nombre"])



### Recorrer la lista para saber cual es la altura minima

minima_altura = 0
flag_primer_personaje = False

for personaje in lista_personajes:
    if personaje["altura"] < minima_altura or flag_primer_personaje == False:
        flag_primer_personaje = True
        minima_altura = personaje["altura"]

for personaje in lista_personajes:
    if personaje["altura"] == minima_altura:
        print(personaje["nombre"])

