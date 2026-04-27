def validar_importe_factura(monto, categoria):
    # Caso de Error: El monto debe ser un número
    if not isinstance(monto, (int, float)):
        raise TypeError("El monto debe ser un número")

    # Caso de Error: Mínimo para Cat A
    if categoria == "A" and monto < 1000:
        raise ValueError("Monto insuficiente para Categoría A")
    
    # Caso Borde: Límite máximo de seguridad
    if monto > 1000000:
        raise ValueError("El monto excede el límite permitido")
        
    return True
