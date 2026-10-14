#M1 Calculadora
print("-->BIENVENIDO A TU PRIMERA CALCULADORA PROFECIONAL<--")

#PRIMERO PEDIMOS LOS DATOS AL USUARIO.Y CONVERTIMOS EL INPUT A DECIMAL(float)
num1 = float(input("Ingresa el primer numero "))
num2 = float(input("ingrea el segundo numero"))

print("\nOperaciones disponibles:")
print("+ : suma")
print("- : resta")
print("* : multiplicacion")
print("/ : division")

operacion = input("Elige uuna operacion (+, -, *, /):")

#estructura de control condicional if / else / elif

if operacion == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operacion == "*":     
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operacion == "/":
    #evitamos que el programa explote si dividen entre cero
    if num2 == 0:
        print("Error : No se puede dividir entre cero.")
    else:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
else: print("Operacion no valida. intente de nuevo.")