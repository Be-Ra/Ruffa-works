def calcular_subtotal(items):
    subtotal = 0
    for item in items:
        subtotal += item["precio"]
    return subtotal
