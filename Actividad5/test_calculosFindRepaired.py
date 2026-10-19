from calculosFindRepaired import calcular_subtotal

def test_calcular_subtotal_multiplica_precio_por_cantidad_de_cada_item():
    items = [{"precio": 1500, "cantidad": 2}, {"precio": 800, "cantidad": 3}]
    assert calcular_subtotal(items) == 5400
