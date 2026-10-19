def calcular_total(precio_unitario, cantidad):
    return precio_unitario * cantidad

def aplicar_descuento (precio_total, descuento):
    return precio_total - (precio_total * descuento / 100)
