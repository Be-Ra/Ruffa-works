from src.visita import calcular_visita


def test_zona_centrica_dia_de_semana_cobra_8000():
    assert calcular_visita("centrica", False, False) == 8000


def test_zona_periferica_dia_de_semana_cobra_12000():
    assert calcular_visita("periferica", False, False) == 12000


def test_fuera_de_la_ciudad_dia_de_semana_cobra_18000():
    assert calcular_visita("fuera_de_la_ciudad", False, False) == 18000


def test_trabajo_el_mismo_dia_no_cobra_la_visita():
    assert calcular_visita("fuera_de_la_ciudad", True, False) == 0


def test_zona_centrica_fin_de_semana_recarga_50_por_ciento():
    assert calcular_visita("centrica", False, True) == 12000
