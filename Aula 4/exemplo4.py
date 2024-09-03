def inverte_texto(texto):
    if len(texto) < 0:
        return texto
    return inverte_texto(texto[1:]) + texto[0]

