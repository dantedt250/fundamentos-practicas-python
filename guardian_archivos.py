import  os 
ARCHIVO_AGENDA = "agenda.txt"

def guardar_contacto(nombre, telefono):
    try:
        # 'with open abre el archivo  lo cierra automáticamente al finalizar el bloque
        # 'a' significa Append(añadir texto al final del archivo)
        with open(ARCHIVO_AGENDA, 'a', encoding='utf-8') as archivo:
            # escribimos el nombre y el teléfono en el archivo separados por una coma
            archivo.write(f"{nombre},{telefono}\n")
        return True
    except Exception as e:
        print(f"Error al guardar en la agenda: {e}")
        return False


def listar_contactos():
    #validación para ver si el archivo existe
    if not os.path.exists(ARCHIVO_AGENDA):
        print("La agenda está vacía. No hay contactos para mostrar (aun no se ha creado el archivo).")
        return
    try:
        print("\n--- Contactos en la Agenda ---")
        # 'r' significa Read (Modo lectura)
        with open(ARCHIVO_AGENDA, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

            if not lineas:
                print("La agenda está vacía. No hay contactos para mostrar.")
                return
            
            for linea in lineas:
                # eliminamos el salto de línea y separamos el nombre y el teléfono por la coma
                nombre, telefono = linea.strip().split(',')
                print(f"Nombre: {nombre}, Teléfono: {telefono}")    

    except Exception as e:
        print(f"Error al leer la agenda: {e}")


# punto de entradaprincipal (pep 8/estandar industrial)
if __name__ == "__main__":
    while True:
        print("\n--- El guardian de archivos txt ---")
        print("1. agregar contacto")
        print("2. listar contactos guardados")
        print("3. salir")

        opcion = input("Seleccione una opción (1-3): ")


        if opcion == '1':
            print("\n [Nuevo contacto]")
            nombre = input("Ingrese el nombre: ").strip()
            telefono = input("Ingrese el teléfono: ").strip()

            #validacion simple para evitar que se guarden contactos vacíos
            if nombre and telefono: # si algun de los dos es vacio, se evalua como False y no se guarda el contacto
                if guardar_contacto(nombre, telefono):
                    print("Contacto guardado exitosamente.")
                
            else:
                print("Nombre y teléfono no pueden estar vacíos. Intente nuevamente.")

        elif opcion == '2':
            listar_contactos()


        elif opcion == '3':
            print("\n Agenda cerrada correctamente. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-3).")