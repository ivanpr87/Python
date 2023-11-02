def crear_cliente(nombre, correo_electronico, saldo, direccion):
    def realizar_compra(cliente, monto):
        if cliente['saldo'] >= monto:
            cliente['saldo'] -= monto
            return True
        else:
            return False

    def verificar_saldo(cliente):
        return cliente['saldo']


    def obtener_direccion(cliente):
        return cliente['direccion']

    def actualizar_direccion(cliente, nueva_direccion):
        cliente['direccion'] = nueva_direccion

    def enviar_correo(cliente, mensaje):
        print(f"Enviando correo a {cliente['correo_electronico']}:\n{mensaje}")

    cliente = {
        'correo_electronico': correo_electronico,
        'saldo': saldo,
        'direccion': direccion,
        'realizar_compra': lambda monto: realizar_compra(cliente, monto),
        'verificar_saldo': lambda: verificar_saldo(cliente),
        'obtener_nombre': lambda: obtener_nombre(cliente),
        'obtener_direccion': lambda: obtener_direccion(cliente),
        'actualizar_direccion': lambda nueva_direccion: actualizar_direccion(cliente, nueva_direccion),
        'enviar_correo': lambda mensaje: enviar_correo(cliente, mensaje),
        '__str__': lambda: nombre
    }

    return cliente




