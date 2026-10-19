from src.visita import calcular_visita


def test_zona_centrica_dia_de_semana_cobra_8000():
    assert calcular_visita("centrica", False, False) == 8000


def test_zona_periferica_dia_de_semana_cobra_12000():
    assert calcular_visita("periferica", False, False) == 12000
