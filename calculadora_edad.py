from datetime import datetime

def calcular_edad_base(año_nacimiento):
    #obtenemos la fecha y hora actual
    hoy = datetime.now()
    #resta simple de años

    edad_estimada = hoy.year - año_nacimiento
    return edad_estimada


if __name__ == "__main__":
    print("--->Calculadora de Edad<---  ")
    try:
        año = int(input("Ingresa tu año de nacimiento (YYYY): "))
        # validacion basica de rango de año
        hoy = datetime.now()
        if 1900 <= año <= hoy.year:
            edad = calcular_edad_base(año)
            print(f"Tienes aproximadamente {edad} años.")
        else:
            print("Por favor, ingresa un año válido entre 1900 y el año actual.")
    except ValueError:
        print("Por favor, ingresa un número válido para el año.")