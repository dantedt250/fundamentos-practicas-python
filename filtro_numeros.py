def clasificar_numeros(lista_texto):
    """
    Recibe una cadena de texto con numeros separados por comas, los convierte en una lista de enteros y los separa en pares e impares.
    """
    pares = []
    impares = []
    #el metodo split() divide la cadena en una lista de subcadenas usando la coma como separador y nos da una lista de strings
    elementos = lista_texto.split(",")

    for elemento in elementos:
        #quitamos espacios en blanco accidentales por ejemplo " 1 , 2 , 3 " se convierte en "1,2,3"
        elemento_limpio = elemento.strip()
        #validamos que reaalmente sea un entero antes de convertirlo
        if elemento_limpio.isdigit():
            numero = int(elemento_limpio)
            #operador residuo para dividir entre dos si es 0 es par si no es impar
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
    return pares, impares

#punto de entrada principal pep8
if __name__ == "__main__":
    print("--->FILTRO DE NUMEROS PARES E IMPARES<---")
    entrada = input("Ingresa una lista de numeros separados por comas: ")


    #validamos que el usuario no haya  dejado la entrada en blanco
    if entrada.strip():
        lista_pares, lista_impares = clasificar_numeros(entrada)
        print("\n ---> RESULTADOS DE LA CLASIFICACION <---")
        print(f"Numeros pares: {lista_pares}")
        print(f"Numeros impares: {lista_impares}")
    else:
        print("No se ingresaron numeros para clasificar.")