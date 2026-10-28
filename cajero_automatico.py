saldo = 1000 #saldo = 1000 # Saldo inicial del cajero automático

def consultar_saldo():
    print(f"---CONSULTA DE SALDO---")
    print(f"Su saldo actual es: ${saldo}")

def depositar_dinero():
    global saldo
    cantidad = float(input("Ingrese la cantidad a depositar:  $"))
    if cantidad > 0:
        saldo += cantidad
        print(f"Depósito exitoso. Su nuevo saldo es: ${saldo}")
    else:
        print("Cantidad inválida. Por favor, ingrese un monto positivo.")

def retirar_dinero():
    global saldo
    cantidad = float(input("Ingrese la cantidad a retirar:  $"))
    if cantidad > 0 and cantidad <= saldo:
        saldo -= cantidad
        print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")
    else:
        print("Cantidad inválida o saldo insuficiente. Por favor, ingrese un monto válido.")

while True:   #bucle infinito
    print("\n--- CAJERO AUTOMÁTICO INTERACTIVO ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        consultar_saldo() #<-- aquí se llama a la función consultar_saldo
    elif opcion == "2":
        depositar_dinero()#<-- aquí se llama a la función depositar_dinero
    elif opcion == "3":
        retirar_dinero()#<-- aquí se llama a la función retirar_dinero
    elif opcion == "4":
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")