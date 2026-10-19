import pytest
from cliente import validar_cliente


# --- Casos normales ---

def test_datos_validos_tipicos_son_aceptados():
    assert validar_cliente("Ana Pérez", "1155667788", "Calle 7 nro 123") is True

def test_nombre_largo_es_aceptado():
    assert validar_cliente("María de los Ángeles Gómez", "1155667788", "Calle 7") is True

def test_telefono_de_diez_digitos_es_aceptado():
    assert validar_cliente("Juan", "2214567890", "Calle 50 nro 800") is True


# --- Casos límite ---

def test_nombre_de_exactamente_3_caracteres_es_aceptado():
    assert validar_cliente("Ana", "1155667788", "Calle 7") is True

def test_nombre_de_2_caracteres_es_rechazado():
    with pytest.raises(ValueError):
        validar_cliente("Al", "1155667788", "Calle 7")

def test_telefono_de_exactamente_8_digitos_es_aceptado():
    assert validar_cliente("Ana", "12345678", "Calle 7") is True

def test_telefono_de_7_digitos_es_rechazado():
    with pytest.raises(ValueError):
        validar_cliente("Ana", "1234567", "Calle 7")

def test_telefono_de_exactamente_15_digitos_es_aceptado():
    assert validar_cliente("Ana", "123456789012345", "Calle 7") is True

def test_telefono_de_16_digitos_es_rechazado():
    with pytest.raises(ValueError):
        validar_cliente("Ana", "1234567890123456", "Calle 7")

def test_direccion_de_un_solo_caracter_es_aceptada():
    assert validar_cliente("Ana", "1155667788", "X") is True


# --- Casos de error ---

def test_nombre_vacio_es_rechazado():
    with pytest.raises(ValueError):
        validar_cliente("", "1155667788", "Calle 7")

def test_nombre_de_solo_espacios_es_rechazado():
    with pytest.raises(ValueError):
        validar_cliente("     ", "1155667788", "Calle 7")

def test_telefono_con_letras_es_rechazado():
    with pytest.raises(ValueError):
        validar_cliente("Ana", "11abc67788", "Calle 7")

def test_telefono_vacio_es_rechazado():
    with pytest.raises(ValueError):
        validar_cliente("Ana", "", "Calle 7")

def test_direccion_vacia_es_rechazada():
    with pytest.raises(ValueError):
        validar_cliente("Ana", "1155667788", "")

def test_direccion_de_solo_espacios_es_rechazada():
    with pytest.raises(ValueError):
        validar_cliente("Ana", "1155667788", "   ")

def test_nombre_none_es_rechazado_de_forma_controlada():
    with pytest.raises(ValueError):
        validar_cliente(None, "1155667788", "Calle 7")
