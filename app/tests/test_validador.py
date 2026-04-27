import pytest
from app.validador import validar_importe_factura

# Caso Exitoso
def test_monto_valido_cat_a():
    assert validar_importe_factura(1500, "A") is True

# Caso de Error
def test_error_monto_insuficiente_b():
    with pytest.raises(ValueError, match="Monto insuficiente para Categoría B"):
        validar_importe_factura(50, "B")

# Casos Borde
def test_limite_maximo_permitido():
    assert validar_importe_factura(1000000, "A") is True

def test_limite_minimo_cat_a():
    assert validar_importe_factura(1000, "A") is True
