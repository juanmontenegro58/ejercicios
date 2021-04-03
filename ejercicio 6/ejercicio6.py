""" 
    Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene
    y su frecuencia. Escribir otra funcion que reciba el diccionario generado con la función anterior y devuelva una
    tupla con la palabra más repetida y su frecuencia.
"""
def main(frase):
    di = {}
    palabra = frase.split(" ")

    for i in palabra:
        if i in di.keys():
            di[i] += 1
        else:
            di[i] = 1
    f = frecuencia(di)
    print(f)

def frecuencia(di):
    palabra = ''
    frec = 0
    for k, v in di.items():
        if v > frec:
            palabra = k
            frec = v
    return (palabra, frec)

frase = "Si no conocéis estos operadores es poco probable que vayáis a necesitarlos, por lo que podéis obviar esta\
parte. Si aún así tenéis curiosidad os diré que estos son operadores que actúan sobre las representaciones\
en binario de los operandos."
main(frase)