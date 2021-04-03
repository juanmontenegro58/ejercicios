""" 
    Escriba la función contar_vocales(oracion) que retorne un diccionario asociando a cada vocal la cantidad de 
    veces que aparece en la oracion. Si una vocal no aparece en la oración, de todos modos debe estar en el 
    diccionario asociada al valor 0:
"""

def contar_vocales(frase):
    dic = {'a': 0, 'e': 0,'i':0,'o':0,'u':0}
    for i in frase:
        if i.lower() in dic.keys():
            dic[i.lower()] += 1
    print(dic)

contar_vocales('Si no conocéis estos operadores es poco probable que vayáis a necesitarlos, por lo que podéis obviar esta\
parte. Si aún así tenéis curiosidad os diré que estos son operadores que actúan sobre las representaciones\
en binario de los operandos.')
