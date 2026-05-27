# DETECTOR DE FRAUDES BANCARIOS

# 1. NUESTROS DATOS (Conceptos de transferencias recientes)
transferencias = [
    "Pago de la colegiatura del mes de mayo",
    "Compra de sustancias sospechosas y armas ilegales",
    "Transferencia a mi hermano por la cena de ayer",
    "Inversión en negocios prohibidos por la ley",
    "Pago del recibo de luz",
    "Venta de documentos falsificados",
    "Compra de artículos escolares",
    "Depósito relacionado con clonación de tarjetas"
]

# 2. NUESTRO MODELO (Palabras de alerta del sistema financiero)
alertas_fraude = [
    "armas",
    "ilegal",
    "prohibidos",
    "sustancias",
    "clonación",
    "falsificados",
    "lavado",
    "fraude"
]

def modelo_ia_banco(concepto):
    concepto_minuscula = concepto.lower()

    # El modelo analiza si la transacción es segura o de riesgo
    for palabra in alertas_fraude:
        if palabra in concepto_minuscula:
            return "ALERTA (Posible Fraude / Cuenta Congelada)"

    return "CONTACTADO (Transacción Exitosa)"

# 3. EVALUACIÓN Y PREDICCIÓN
print("--- DETECTOR DE FRAUDES BANCARIOS ---")

for i, concepto in enumerate(transferencias, 1):
    prediccion = modelo_ia_banco(concepto)
    print(f"Transacción {i}: '{concepto}' -> RESULTADO: {prediccion}")
