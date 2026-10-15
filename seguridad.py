contraseña_correcta = "1234"
intentos_restantes = 3

while intentos_restantes > 0:
    intentos_restantes -= 1
    intento_usuario = input("\nIngrese la contraseña secreta: ")
    
    if intento_usuario == contraseña_correcta:
        print("¡Acceso concedido!")
        break
else:
    print(f"¡Acceso denegado! . te quedan {intentos_restantes} intentos.")

if intentos_restantes == 0:
    print("Has agotado todos los intentos. La cuenta ha sido bloqueada.") 
