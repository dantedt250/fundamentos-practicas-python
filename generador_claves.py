import random
import string

def generar_contrasea_base(longitud):
    #combinamos letras minusculas, mayúsculas y numeros para la version 1.0
    caracteres = string.ascii_lowercase + string.digits

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña



if __name__ == "__main__":
    print("--->Generador de contraseñas<---")
    try:
        largo = int(input("De cuantos caracteres quieres que sea tu contraseña: "))
        if largo >= 4:
            clave = generar_contrasea_base(largo)
            print(f"Tu contraseña generada es: {clave}")
        else:
            print("La contraseña debe tener al menos 4 caracteres.")

    except ValueError:
        print("Por favor, ingresa un número válido.")