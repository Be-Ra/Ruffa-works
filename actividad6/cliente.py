def validar_cliente(nombre, telefono, direccion):
    """Valida los datos de un cliente. Lanza ValueError si algo es inválido."""
    if not isinstance(nombre, str) or len(nombre.strip()) < 3:
        raise ValueError("El nombre debe tener al menos 3 caracteres")

    if not isinstance(telefono, str) or not telefono.isdigit() or not 8 <= len(telefono) <= 15:
        raise ValueError("El teléfono debe tener entre 8 y 15 dígitos")

    if not isinstance(direccion, str) or not direccion.strip():
        raise ValueError("La dirección no puede estar vacía")

    return True
