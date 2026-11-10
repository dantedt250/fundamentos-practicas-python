import random
import string

def generar_contraseña_avanzada(logitud):
    #mejora combinamos letras mayusculas, minusculas, numeros y simbolos
    caracteres = (
        string.ascii_lowercase + 
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    contraseña = ''.join(random.choice(caracteres) for _ in range(logitud))
    return contraseña

if __name__ == "__main__":
    print("--->Generador de contraseñas<---")
    try:
        largo = int(input("De cuantos caracteres quieres que sea tu contraseña: "))
        if largo >= 8:
            clave = generar_contraseña_avanzada(largo)
            print(f"Tu contraseña generada es: {clave}")
        else:
            print("La contraseña debe tener al menos 8 caracteres.")

    except ValueError:
        print("Por favor, ingresa un número válido.")