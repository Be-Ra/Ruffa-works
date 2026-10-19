from calculos import calcular_total

def test_calcular_total_multiplica_precio_por_cantidad():
    resultado = calcular_total(1500, 3)
    assert resultado == 4500
