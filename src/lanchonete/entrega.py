def calcular_taxa_entrega(distancia_km: float) -> float:
    """
    Regras de negócio para taxa de entrega:
    - Distância deve ser > 0.
    - Até 2 km:            grátis (R$ 0,00)
    - De 2,01 até 5 km:    R$ 5,00
    - De 5,01 até 10 km:   R$ 10,00
    - Acima de 10 km:      não realizamos entrega (ValueError).
    """
    if distancia_km <= 0:
        raise ValueError("Distância deve ser maior que zero.")
    if distancia_km > 10:
        raise ValueError("Entrega não disponível para distâncias acima de 10 km.")
    if distancia_km <= 2:
        return 0.00
    if distancia_km <= 5:
        return 5.00
    return 10.00
