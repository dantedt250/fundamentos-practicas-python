class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email


mis_contactos = []


print( "Introduce un nuevo contacto:")
Nombre = input("Nombre: ")
Telefono = input("Teléfono: ")
Email = input("Email: ")


nuevo_contacto = Contacto(Nombre, Telefono, Email)
mis_contactos.append(nuevo_contacto)

print(f"Contacto agregado: {nuevo_contacto.nombre}, {nuevo_contacto.telefono}, {nuevo_contacto.email}")

total_contactos = len(mis_contactos)
print(f"Total de contactos en la agenda: {total_contactos}")