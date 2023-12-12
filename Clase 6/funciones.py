
def mostrar_personajes(lista_personajes:list, clave:str = "", valor:int = 0):
    print("Lista de personajes: ")

    if(clave != "" and valor != 0):
        for personaje in lista_personajes:
            if personaje[clave] == valor:
                mostrar_personaje(personaje)
    else:
        for personaje in lista_personajes:
            mostrar_personaje(personaje)

# def mostrar_algunos_personajes(lista_personajes:list, clave:str, valor:int):
#     for personaje in lista_personajes:
#         if personaje[clave] == valor:
#             mostrar_personaje(personaje)

def mostrar_personaje(un_personaje : dict):
    print(f"Nombre: {un_personaje ['nombre']} -", 
          f"Identidad: {un_personaje['identidad']} -"  , 
          f"Empresa: {un_personaje['empresa']} ",
          f"Altura: {un_personaje['altura']}",
          f"Peso: {un_personaje['peso']}")


