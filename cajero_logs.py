from datetime import datetime
#constantes globsles pep8
ARCHIVO_LOG = "transacciones.log"

#funcion auditoria
def REGISTRAR_LOG(mensaje):
    """Guarda un evento en el archivo de log con la fecha y hora actual."""
    try:
        #obtener la fecha y hora actual
        marca_tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #abrimos en modo a (append) para agregar al final del archivo
        with open(ARCHIVO_LOG, "a",encoding="utf-8") as archivo:
            archivo.write(f"{marca_tiempo} - {mensaje}\n")
    except Exception as e:
        print(f"Error al registrar el log: {e}")

# funciones de operaciones de cajero automático
def consltar_saldo(saldo):
    print(f"Su saldo actual es: ${saldo:.2f}")
    REGISTRAR_LOG(f"Consulta de saldo: ${saldo:.2f}")


def depositar (saldo, monto):
    if monto > 0:
        saldo += monto
        print(f"Depósito exitoso. Su nuevo saldo es: ${saldo:.2f}")
        REGISTRAR_LOG(f"Depósito realizado: ${monto:.2f}. Nuevo saldo: ${saldo:.2f}")
    else:
        print("Monto inválido. Por favor, ingrese un monto positivo.")
        REGISTRAR_LOG(f"ERROR DE ENTRADA: Monto inválido ingresado para depósito.")
    return saldo

def retirar(saldo, monto):
    if monto <= 0:
        print("Monto inválido. Por favor, ingrese un monto positivo.")
        REGISTRAR_LOG(f"ERROR DE ENTRADA: Monto inválido ingresado para retiro.")
    elif monto > saldo:
        print("Fondos insuficientes.")
        REGISTRAR_LOG(f"ERROR DE ENTRADA: Intento de retiro con fondos insuficientes.")
    else:
        saldo -= monto
        print(f"Retiro exitoso. Su nuevo saldo es: ${saldo:.2f}")
        REGISTRAR_LOG(f"Retiro exitoso: ${monto:.2f}. Nuevo saldo: ${saldo:.2f}")
    return saldo


if __name__ == "__main__":
    saldo_actual = 1000.00  # Saldo inicial
    REGISTRAR_LOG("Inicio de sesión en el cajero automático.")
    while True:
        print("\n---Cajero automatico 2.0---:")
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
                REGISTRAR_LOG(f"ERROR DE ENTRADA: Monto inválido ingresado para depósito.")  
        elif opcion == "3":
            try:
                cantidad = float(input("Ingrese el monto a retirar: "))
                saldo_actual = retirar(saldo_actual, cantidad)
            except ValueError:
                print("Monto inválido. Por favor, ingrese un número válido.")
                REGISTRAR_LOG(f"ERROR DE ENTRADA: Monto inválido ingresado para retiro.")
        elif opcion == "4":
            print("Gracias por usar el cajero automático hasta luego.")
            REGISTRAR_LOG("Cierre de sesión en el cajero automático.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")