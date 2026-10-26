import random

numero_secreto = random.randint(1, 100)
#print(numero_secreto)  # Esto es solo para fines de depuración, puedes eliminarlo en la versión final

intentos_restantes = 7



while intentos_restantes > 0:
    print(f"\nTienes {intentos_restantes} intentos restantes.")
    intento_usuario = int(input("Adivina el número (entre 1 y 100): "))

    if intento_usuario == numero_secreto:
        print("¡Felicidades! ¡Has adivinado el número secreto!")
        break
    elif intento_usuario < numero_secreto:
        print("El numero secreto es mas alto.")
    else:
        print("El numero secreto es mas bajo.")

    intentos_restantes -= 1

if intentos_restantes == 0:
    print(f"Lo siento, no has adivinado el número secreto. Era: {numero_secreto}")