texto_usuario = input("Ingrese un texto: ")
total_caracteres = len(texto_usuario)
lista_palabras = texto_usuario.split()
total_palabras = len(lista_palabras)

print("El texto ingresado tiene", total_caracteres, "caracteres (incluyendo espacios en blanco).")
print("El texto ingresado tiene", total_palabras, "palabras.")

print("Las palabras ingresadas son:")
for palabra in lista_palabras:
    print(f"- {palabra}")
    