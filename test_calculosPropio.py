from calculosPropio import calcular_total, aplicar_descuento

def test_aplicar_descuento_del_diez_por_ciento_reduce_el_monto():
    assert aplicar_descuento(1000, 10) == 900

def test_aplicar_descuento_cero_devuelve_el_monto_original():
    assert aplicar_descuento(1000, 0) == 1000

def test_aplicar_descuento_cien_por_ciento_devuelve_cero():
    assert aplicar_descuento(1000, 100) == 0
