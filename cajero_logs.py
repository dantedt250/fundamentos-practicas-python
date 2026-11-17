def consltar_saldo(saldo):
    print(f"Su saldo actual es: ${saldo:.2f}")


def depositar (saldo, monto):
    if monto > 0:
        saldo += monto
        print(f"Depósito exitoso. Su nuevo saldo es: ${saldo:.2f}")
    else:
        print("Monto inválido. Por favor, ingrese un monto positivo.")
    return saldo

def retirar(saldo, monto):
    if monto <= 0:
        print("Monto inválido. Por favor, ingrese un monto positivo.")
    elif monto > saldo:
        print("Fondos insuficientes.")
    else:
        saldo -= monto
        print(f"Retiro exitoso. Su nuevo saldo es: ${saldo:.2f}")
    return saldo


if __name__ == "__main__":
    saldo_actual = 1000.00  # Saldo inicial

    while True:
        print("\n---Cajero automatico---:")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            consltar_saldo(saldo_actual)
        elif opcion == "2":
            try:
                cantidad = float(input("Ingrese el monto a depositar: "))
                saldo_actual = depositar(saldo_actual, cantidad)
            except ValueError:
                print("Monto inválido. Por favor, ingrese un número válido.")    
        elif opcion == "3":
            try:
                cantidad = float(input("Ingrese el monto a retirar: "))
                saldo_actual = retirar(saldo_actual, cantidad)
            except ValueError:
                print("Monto inválido. Por favor, ingrese un número válido.")
        elif opcion == "4":
            print("Gracias por usar el cajero automático hasta luego.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")