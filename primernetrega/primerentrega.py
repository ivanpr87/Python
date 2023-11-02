""""crear un programa que permita emular el registro y login de usuarios en base de datos . tenes que ulitizar funciones, diccioanarios, bucles y condicionales"""


# Inicializar un diccionario para almacenar usuarios y contraseñas
usuarios = {}

# Función para registrar un nuevo usuario
def registrar_usuario():
    print("Registro de nuevo usuario")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    # Verificar si el usuario ya existe en la base de datos
    if usuario in usuarios:
        print("El usuario ya está registrado. Introduce otro nombre de usuario.")
    else:
        usuarios[usuario] = contraseña
        print("Usuario registrado con éxito.")

# Función para mostrar la información de un usuario
def mostrar_usuario(usuario):
    if usuario in usuarios:
        print(f"Nombre de usuario: {usuario}")
        print(f"Contraseña: {usuarios[usuario]}")
    else:
        print("Usuario no encontrado.")

# Función para iniciar sesión
def iniciar_sesion():
    print("Iniciar sesión")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Ingreso exitoso. ¡Bienvenido!")
    else:
        print("Credenciales incorrectas. Inténtalo de nuevo.")

# Función principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Registrar nuevo usuario")
        print("2. Mostrar información de un usuario")
        print("3. Iniciar sesión")
        print("4. Salir")

        opcion = input("Selecciona una opción (1/2/3/4): ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            usuario = input("Introduce el nombre de usuario: ")
            mostrar_usuario(usuario)
        elif opcion == "3":
            iniciar_sesion()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Introduce 1, 2, 3 o 4.")


main()
