TARIFAS = {
    "centrica": 8000,
    "periferica": 12000,
    "fuera_de_la_ciudad": 18000,
}


def calcular_visita(zona, trabajo_mismo_dia, es_fin_de_semana):
    return TARIFAS[zona]
