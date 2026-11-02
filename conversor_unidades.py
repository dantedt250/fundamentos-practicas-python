def celcius_to_fahrenheit(celsius):
    #formula : (celsius * 9/5) + 32
    result = (celsius * 9/5) + 32
    return result


def kilometers_to_miles(kilometers):
    #formula : kilometers * 0.621371
    result = kilometers * 0.621371
    return result

def mostrar_menu():
    while True:
        print("Seleccione la conversión que desea realizar:")
        print("1. Temperatura - Celsius a Fahrenheit")
        print("2. Distancia - Kilómetros a Millas")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "3":
            print("Gracias por usar el conversor de unidades. ¡Hasta luego!")
            break

        if opcion in ["1", "2"]:
            try: 
                if opcion == "1":
                    celsius = float(input("Ingrese la temperatura en Celsius: "))
                    fahrenheit = celcius_to_fahrenheit(celsius)
                    print(f"{celsius}°C son {fahrenheit}°F")

                elif opcion == "2":
                        km = float(input("Ingrese la distancia en kilómetros: "))
                        miles = kilometers_to_miles(km)
                        print(f"{km} km son {miles} millas")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")

    #al final de todo el archivo llamamos a la función mostrar_menu() para iniciar el programa
   
   

mostrar_menu()
