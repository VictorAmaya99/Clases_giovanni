# 6-
# Se nos pide realizar un programa que le pida al usuario una N cantidad de veces y
# calcular la máxima diferencia en la secuencia de números ingresada.

lista_numeros = []
TAM = 10

for i in range(TAM):
    numero_ingresado = int(input("Ingrese un numero: "))
    lista_numeros.append(numero_ingresado)
print(lista_numeros)

maximo_numero = None
flag = True

for numero in lista_numeros:
    if flag == True or numero > maximo_numero:
        maximo_numero = numero
        flag = False
print(f"El maximo numero es: {maximo_numero}")