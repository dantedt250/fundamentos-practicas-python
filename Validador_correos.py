def validar_correo(correo):
    try:
        #quitamos espacios en blanco al inicio y al final del correo
        correo = correo.strip()
        if correo.count("@") != 1:
            return False, "El correo debe contener exactamente un '@'."

        usuario, dominio = correo.split("@")
        # Validamos el usuario no este vacio
        if len(usuario) == 0:
            return False, "El usuario (antes del @) no puede estar vacío."

        #el dominio debe terminar estrictamente con .com
        if not dominio.endswith(".com"):
            return False, "El dominio debe terminar con '.com'."
        #si pasa todas las pruebas el correo es valido
        return True, "El correo es válido."
    
    except Exception as e:
        return False , f"Error inesperado: {str(e)}"






print("---> Validación de correos electrónicos <---")
entrada_usuario = input("Ingrese un correo electrónico para validar: ")

es_valido, mensaje = validar_correo(entrada_usuario)

if es_valido:
    print(f"Resultado: {mensaje}")
else:
    print(f"Resultado: {mensaje}")