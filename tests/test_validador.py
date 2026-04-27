import pytest
from app.validador import validar_importe_factura

# 1. CASO EXITOSO
def test_monto_valido_exitoso():
    # Un monto de 5000 para Cat A es válido (mínimo es 1000)
    assert validar_importe_factura(5000, "A") is True

# 2. CASO DE ERROR
def test_error_monto_insuficiente():
    # Falla porque 500 es menor al mínimo de 1000 para Cat A
    with pytest.raises(ValueError, match="Monto insuficiente"):
        validar_importe_factura(500, "A")

# 3. CASO BORDE (Edge Case)
def test_limite_maximo_borde():
    # El límite exacto de 1.000.000 debe ser permitido
    assert validar_importe_factura(1000000, "A") is True
