TARIFAS = {
    "centrica": 8000,
    "periferica": 12000,
    "fuera_de_la_ciudad": 18000,
}


def calcular_visita(zona, trabajo_mismo_dia, es_fin_de_semana):
    if zona not in TARIFAS:
        raise ValueError(f"Zona inexistente: {zona}")
    if trabajo_mismo_dia:
        return 0
    valor = TARIFAS[zona]
    if es_fin_de_semana:
        valor = valor * 1.5
    return valor
