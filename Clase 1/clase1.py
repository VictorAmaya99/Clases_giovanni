
nombre = input("Ingrese su nombre: ")
peso = float(input("Ingrese su peso: "))

if peso > 75:
    peso = peso * 1.20
else:
    peso = peso * 0.8

print(f"su nombre es: {nombre}")
print(f"su peso es: {peso:.2f}")