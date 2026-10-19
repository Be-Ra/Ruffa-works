def validar_datos_cliente(nombre_cliente, telefono_cliente, direccion_cliente):
    """Versión de novato: devuelve True si los datos son válidos, False si no."""

    # El nombre tiene que tener al menos 3 caracteres
    if len(nombre_cliente) > 3:
        nombre_ok = True
    else:
        nombre_ok = False

    # El teléfono tiene que tener entre 8 y 15 dígitos
    if len(telefono_cliente) > 8 and len(telefono_cliente) < 15:
        telefono_ok = True
    else:
        telefono_ok = False

    # La dirección no puede estar vacía
    if direccion_cliente != "":
        direccion_ok = True
    else:
        direccion_ok = False

    return nombre_ok and telefono_ok and direccion_ok
