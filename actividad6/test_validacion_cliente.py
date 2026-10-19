from validacion_cliente import validar_datos_cliente


# --- Casos normales ---

def test_cliente_con_datos_correctos_es_valido():
    assert validar_datos_cliente("Ana Pérez", "1155667788", "Calle 7 nro 123") is True

def test_cliente_con_nombre_largo_es_valido():
    assert validar_datos_cliente("María de los Ángeles Gómez", "1155667788", "Calle 7") is True

def test_cliente_con_telefono_de_10_digitos_es_valido():
    assert validar_datos_cliente("Juan", "2214567890", "Calle 50 nro 800") is True


# --- Casos límite ---

def test_nombre_con_tres_letras_es_valido():
    assert validar_datos_cliente("Ana", "1155667788", "Calle 7") is True

def test_nombre_con_dos_letras_no_es_valido():
    assert validar_datos_cliente("Al", "1155667788", "Calle 7") is False

def test_telefono_con_8_digitos_es_valido():
    assert validar_datos_cliente("Carlos", "12345678", "Calle 7") is True

def test_telefono_con_7_digitos_no_es_valido():
    assert validar_datos_cliente("Carlos", "1234567", "Calle 7") is False

def test_telefono_con_15_digitos_es_valido():
    assert validar_datos_cliente("Carlos", "123456789012345", "Calle 7") is True

def test_telefono_con_16_digitos_no_es_valido():
    assert validar_datos_cliente("Carlos", "1234567890123456", "Calle 7") is False

def test_direccion_con_un_caracter_es_valida():
    assert validar_datos_cliente("Carlos", "1155667788", "X") is True


# --- Casos de error ---

def test_nombre_vacio_no_es_valido():
    assert validar_datos_cliente("", "1155667788", "Calle 7") is False

def test_nombre_con_solo_espacios_no_es_valido():
    assert validar_datos_cliente("     ", "1155667788", "Calle 7") is False

def test_telefono_con_letras_no_es_valido():
    assert validar_datos_cliente("Carlos", "11abc67788", "Calle 7") is False

def test_telefono_vacio_no_es_valido():
    assert validar_datos_cliente("Carlos", "", "Calle 7") is False

def test_direccion_vacia_no_es_valida():
    assert validar_datos_cliente("Carlos", "1155667788", "") is False

def test_direccion_con_solo_espacios_no_es_valida():
    assert validar_datos_cliente("Carlos", "1155667788", "   ") is False

def test_nombre_none_no_es_valido_y_no_rompe_el_programa():
    assert validar_datos_cliente(None, "1155667788", "Calle 7") is False
