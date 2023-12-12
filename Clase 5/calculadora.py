
# def sumar():
#     '''
#     funcion que se encarga de pedir dos numeros, sumarlos y mostrar el resultado
#     '''
#     #Desarrollo de la funcion
#     numero_uno = int(input("Ingrese el primer numero: "))
#     numero_dos = int(input("Ingrese el segundo numero: "))
#     suma = numero_uno + numero_dos
#     print("La suma entre {0} y {1} es: {2}".format(numero_uno, numero_dos,suma))

# def restar():
#     '''
#     funcion que se encarga de pedir dos numeros, restarlos y mostrar el resultado
#     '''
#     numero_uno = int(input("Ingrese el primer numero: "))
#     numero_dos = int(input("Ingrese el segundo numero: "))
#     resta = numero_uno - numero_dos
#     print("La resta entre {0} y {1} es: {2}".format(numero_uno, numero_dos,resta))

# def dividir():
#     '''
#     funcion que se encarga de peir dos numeros, dividirlos y mostrar el resultado.
#     en caso de que el segundo numero sea cero no va a poder dividirlos ya que no
#     existe la division por cero
#     '''
#     numero_uno = int(input("Ingrese el primer numero: "))
#     numero_dos = int(input("Ingrese el segundo numero: "))
#     #No se puede dividir por cero
#     if numero_dos != 0:
#         division = numero_uno / numero_dos
#         print("La division entre {0} y {1} es: {2}".format(numero_uno, numero_dos,division))
#     else:
#         print("No se puede dividir por cero")

# def multiplicar():
#     '''
#     funcion que se encarga de pedir dos numeros, multiplicarlos y mostrar el resultado
#     '''
#     numero_uno = int(input("Ingrese el primer numero: "))
#     numero_dos = int(input("Ingrese el segundo numero: "))
#     multiplicar = numero_uno * numero_dos
#     print("La multiplicacion entre {0} y {1} es: {2}".format(numero_uno, numero_dos,multiplicar))


###Parametrizacion 

def sumar(numero_uno, numero_dos):
    suma = numero_uno + numero_dos
    return suma

def restar(numero_uno, numero_dos):    
    resta = numero_uno - numero_dos
    return resta

def dividir(numero_uno, numero_dos):
    division = None
    if numero_dos != 0:
        division = numero_uno / numero_dos
    return division

def multiplicar(numero_uno, numero_dos):
    multiplicar = numero_uno * numero_dos
    return multiplicar

def pedir_entero(mensaje, limite_inferior, limite_superior):
    numero = int(input(mensaje))
    while numero < limite_inferior or numero > limite_superior:
        numero = int(input("Error, reingrese numero: "))
    return numero

def manipular_menu_principal():
    '''
    funcion que muestra el menu principal me pide una opcion y manipula la calculadora
    '''
    repeticion = True

    while repeticion:
        n1 = pedir_entero("Ingrese el primer numero: ", -1000, 1000)
        n2 = pedir_entero("Ingrese el segundo numero: ", 1000, 75000)
        
        print()
        opcion = pedir_entero("Bienvenido a la calculadora magica \n1-Sumar\n2-Restar\n3-Dividir\n4-Multiplicar\n5-Salir\n-Ingrese una opcion: ", 1, 5)

        if opcion == 1:
            #Llamada de la funcion
            resultado = sumar(n1, n2)#Parametros actuales
            print(f"El resultado de la suma es:  {resultado}")
       
        elif opcion == 2: 
            resultado = restar(n1, n2)
            print(f"El resultado de la resta es: {resultado}")
                
        elif opcion == 3:
            resultado = dividir(n1, n2)
            if resultado != None:
                print(f"El resultado de la division es: {resultado}")
            else:
                print("No se puede dividir por cero")    

        elif opcion == 4:
            resultado = multiplicar(n1, n2)
            print(f"El resultado de la multiplicacion es: {resultado}")
            
        elif opcion == 5:
            print("Saliendo")
            repeticion = False
        else:
            print("opcion incorrecta")


manipular_menu_principal()