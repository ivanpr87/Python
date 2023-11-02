from paginadecompras.cliente import crear_cliente


"""
prueba de metodos
"""
cliente1 = crear_cliente("yo yo", "yo@gmail.com", 600, "Calle 123")
print(cliente1['verificar_saldo']())  # Salida: 999
cliente1['realizar_compra'](500)
print(cliente1['verificar_saldo']())  # Salida: 0
cliente1['actualizar_direccion']("Calle 345")
print(cliente1['obtener_direccion']()) # Salida: Calle 345
cliente1['enviar_correo']("Hola, este es un mensaje de prueba.")
print(cliente1['__str__']())



