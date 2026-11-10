from datetime import date, datetime

def calcular_edad_exacta (fecha_nacimiento):
    hoy = datetime.now()
    años = hoy.year - fecha_nacimiento.year


    if(hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        años -= 1
        meses = ((12 - fecha_nacimiento.month) + hoy.month-1)
    else:
        meses = hoy.month - fecha_nacimiento.month


    if hoy.day >= fecha_nacimiento.day:
        dias = hoy.day - fecha_nacimiento.day
    else:
        dias = (30-fecha_nacimiento.day) + hoy.day

    return años, meses, dias

if __name__ == "__main__":
    print("--->Calculadora de Edad<---  ")
    try:
        entrada = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
        fecha_nacimiento = datetime.strptime(entrada, "%Y-%m-%d").date()
        fecha_hoy =  date.today()

        if fecha_nacimiento <= fecha_hoy and fecha_nacimiento.year >= 1900:
            años, meses, dias = calcular_edad_exacta(fecha_nacimiento)
            print(f"Su edad exacta es: {años} años, {meses} meses y {dias} días.")
        else:
            print("La fecha de nacimiento ingresada no es válida. Asegúrese de que sea una fecha pasada y posterior a 1900.")

    except ValueError:
        print("Formato de fecha inválido. Por favor, ingrese la fecha en el formato YYYY-MM-DD.")