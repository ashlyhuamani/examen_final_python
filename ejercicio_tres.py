"""
crear un funcion que me retorne un diccioonario de la cantidad de vocales que aparecen en un texto pasado por parametro el diccionario debera ser credo por comprension de diccionarios
ejm:
entrada: eucalipto
salida: {e:1,u:1,a:1,i:1,o:1}
"""
def contar_vocales(texto):
    vocales = "aeiou"
    return {vocal: texto.count(vocal) for vocal in texto if vocal in vocales}

# Ejemplo de uso
entrada = "eucalipto"
resultado = contar_vocales(entrada)
print(resultado)