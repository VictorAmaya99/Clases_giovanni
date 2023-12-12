def sumar(numero_uno, numero_dos):#parametros formales
    
    
    numero_uno = int(input("Ingrese el primer numero: "))
    numero_dos = int(input("Ingrese el segundo numero: "))
    suma = numero_uno + numero_dos
    print("La suma entre {0} y {1} es: {2}".format(numero_uno, numero_dos,suma))

sumar(3, 4)