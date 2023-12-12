# 5-
# Para una veterinaria se pide clasificar el ingreso de pacientes hasta que el usuario
# quiera (se limita a 1 perrito por ingreso), se les pide:
# nombre, precio de la consulta (validar entre 500$ y 2500$) raza: (validar entre caniche,
# ovejero, siberiano), edad (validar 1 a 15) y peso (entre 25 y 40 kilos) determinar:

# 1. Generar un listado con todos los datos de los pacientes ordenados por edad.
# 2. Generar un listado de los perros que pesen más de 30 kilos y ordenarla por
# nombre.
# 3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de
# impuesto por ingresos brutos e informarlo.
# 4. Informar el nombre y el peso del perro con más peso.

from os import system
system("cls")

seguir = "si"
acumulador_precio = 0
ingresos_brutos = 0.21
precio_impuesto = 0

lista_perritos = []

while seguir == "si":
    nombre = input("Ingrese el nombre del perro: ")
    while True:
        precio = input("Ingrese el precio de la consulta: ")
        if(precio.isdigit()):
            precio = int(precio)
            if not(precio <= 500 or precio >= 2500):
                break
            else:
                print("Error, precio fuera del rango, reingrese precio: ")
        else:
            print("Error, eso no es un numero, reigrese precio: ")
    raza = input("Ingrese raza del perro (caniche, ovejero o siberiano): ")
    while raza not in ("caniche", "ovejero", "siberiano"):
        raza = input("Error, reingrese raza del perro (caniche, ovejero o siberiano): ")
    while True:
        edad = input("Ingrese la edad del perro (1 a 15): ")
        if(edad.isdigit()):
            edad = int(edad)
            if not(edad <= 1 or edad >= 15):
                break
            else:
                print("Error, edad fuera del rango, reingrese edad: ")
        else:
            print("Error, eso no es un numero, reigrese edad: ")
    while True:
        peso = input("Ingrese el peso del perro: ")
        if(peso.isdigit()):
            peso = int(peso)
            if not(peso <= 25 or peso >= 40):
                break
            else:
                print("Error, peso fuera del rango, reingrese peso: ")
        else:
            print("Error, eso no es un numero, reigrese peso: ")
    
    lista_perritos.append([nombre, precio, raza, edad, peso])
          
    listado_por_edad = sorted(lista_perritos, key=lambda x:x[3])

    if peso >= 30:
       listado_por_peso = sorted(lista_perritos, key=lambda x:x[4])

    # 3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de
    # impuesto por ingresos brutos e informarlo.

    acumulador_precio += precio
    if acumulador_precio >= 5000:
       precio_impuesto = acumulador_precio * ingresos_brutos

    # 4. Informar el nombre y el peso del perro con más peso.

    maximo_peso = None
    flag = True
    nombre_perro_mas_peso = None

    for perrito in lista_perritos:
        if flag == True or perrito[4] > maximo_peso:
            maximo_peso = perrito[4]
            nombre_perro_mas_peso = perrito[0]
            flag = False
    

    seguir = input("Desea continuar: ")

print(listado_por_edad)
print("--------------------------------------------")
print(listado_por_peso)
print("--------------------------------------------")
print(f"El impuesto por ingresos brutos es de: {precio_impuesto:.2f}")
print(f"El nombre del perrito con mas peso es: {nombre_perro_mas_peso}, con un peso de {maximo_peso}")

