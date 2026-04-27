
def validar_importe_factura(monto, categoria):
    """
    Valida el importe de una factura según la categoría fiscal.
    """
    if not isinstance(monto, (int, float)):
        raise TypeError("El monto debe ser un número")

    if monto > 1000000:
        raise ValueError("El monto excede el límite permitido")
    
    if categoria == "A" and monto < 1000:
        raise ValueError("Monto insuficiente para Categoría A")
    
    if categoria == "B" and monto < 100:
        raise ValueError("Monto insuficiente para Categoría B")
        
    return True
