#para crear una lisa solo es necesario poner el nombre de la lista y los corchetes
agenda = []

while True:   #bucle infinito 
    print ("\n- Agenda de Contatos -")
    print ("1 - añadir contato")
    print ("2 - mostrar contactos")
    print ("3 - buscar contacto")
    print ("4 - Salir")
    opcion = input("Seleccione una opción: ")
    if opcion not in ["1", "2", "3", "4"]:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    
    if opcion == "1":
        #se toma el nombre y el telefono del contacto y se guarda en su respectiva variable
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono del contacto: ")

        # se crea un diccionario con los datos de este contacto en especifico
        #un diccionario se crea definiendo el nombre de la variable y los corchetes, dentro de los corchetes se ponen las llaves y dentro de las llaves se ponen los datos que queremos guardar en el diccionario
        nuevo_contacto = {"nombre": nombre, "telefono": telefono}

        #guardamos el diccionario en la lista global agenda
        agenda.append(nuevo_contacto)
        print(f"Contacto {nombre} agregado exitosamente.")



    elif opcion == "2":
        if len(agenda) == 0:
            print("No hay contactos en la agenda.")
        else:
            print("\n- Lista de Contactos -")
            #ciclo for para recorrer la lista de contactos y mostrar los datos de cada contacto
            for contacto in agenda:
                print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")



    elif opcion == "3":
        busqueda = input("Ingrese el nombre del contacto a buscar: ")
        encontrado = False  # Bandera para indicar si se encontró el contacto

        for contacto in agenda:#ciclo for para recorrer la lista de contactos y buscar el contacto que coincida con el nombre ingresado por el usuario
            if contacto['nombre'].lower() == busqueda.lower():
                print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
                encontrado = True
                break  # Salimos del bucle una vez que encontramos el contacto

        if not encontrado: #tambien se puede poner if encontrado == False:
            print("Contacto no encontrado.")





    
    elif opcion == "4":
        print("Saliendo de la agenda...")
        break  #salimos del bucle infinito y terminamos el programa


