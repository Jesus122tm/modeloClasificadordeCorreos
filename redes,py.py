# moderador de redes sociales

# 1. NUESTROS DATOS (Comentarios en una publicación)
comentarios_nuevos = [
    "Hola, qué buen video",
    "Eres un tonto",
    "Me gustó mucho tu contenido",
    "Qué basura de publicación",
    "Excelente trabajo",
    "Eres muy feo",
    "Gran información, gracias",
    "Qué idiota eres"
]

# 2. NUESTRO MODELO (Palabras prohibidas por la comunidad)
palabras_toxicas = [
    "tonto",
    "basura",
    "idiota",
    "feo",
    "estúpido",
    "payaso",
    "inútil",
    "ridículo"
]

def modelo_ia_moderador(comentario):
    comentario_minuscula = comentario.lower()

    # El modelo busca si hay lenguaje ofensivo
    for palabra in palabras_toxicas:
        if palabra in comentario_minuscula:
            return "BLOQUEADO (Tóxico)"  # Predicción 1

    return "APROBADO (Seguro)"  # Predicción 2

# 3. EVALUACIÓN Y PREDICCIÓN
print("--- MODERADOR DE REDES SOCIALES ---")

for i, comentario in enumerate(comentarios_nuevos, 1):
    prediccion = modelo_ia_moderador(comentario)
    print(f"Comentario {i}: '{comentario}' -> ESTADO: {prediccion}")
