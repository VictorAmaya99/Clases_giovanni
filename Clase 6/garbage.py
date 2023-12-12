# def mostrar_altura_minima():
#     minima_altura = 0
#     flag_primer_personaje = False

#     for personaje in lista_personajes:
#         if personaje["altura"] < minima_altura or flag_primer_personaje == False:
#             flag_primer_personaje = True
#             minima_altura = personaje["altura"]

#     for personaje in lista_personajes:
#         if personaje["altura"] == minima_altura:
#             #print(f"El personaje con la altura minima es: {personaje['nombre']}, con una altura de: {minima_altura}")
#             mostrar_personaje(personaje)

# def calcular_maximo_peso(lista:list)->int:
#     maximo_peso = 0
#     flag_primer_personaje = False

#     for personaje in lista :
#         if personaje["peso"] > maximo_peso or flag_primer_personaje == False :
#             flag_primer_personaje = True
#             maximo_peso = personaje["peso"]
#     return maximo_peso

# def mostrar_peso_maximo(lista:list):
#     maximo_peso = calcular_maximo_peso(lista)
    
#     print("Personaje con maximo peso: ")
#     for personaje in lista:
#         if personaje["peso"] == maximo_peso:
#             mostrar_personaje(personaje)
