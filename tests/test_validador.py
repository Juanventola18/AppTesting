import pytest
from app.validador import validar_importe_factura

# 1. CASO EXITOSO
def test_monto_valido_exitoso():
    # Un monto normal que cumple las reglas
    assert validar_importe_factura(5000, "A") is True

# 2. CASO DE ERROR
def test_error_monto_insuficiente():
    # Falla porque el mínimo para Cat A es 1000
    with pytest.raises(ValueError, match="Monto insuficiente"):
        validar_importe_factura(500, "A")

# 3. CASO BORDE (Edge Case)
def test_limite_maximo_borde():
    # El límite exacto permitido por el sistema
    assert validar_importe_factura(1000000, "A") is True
