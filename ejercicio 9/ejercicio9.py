""" 
    El diccionario paises asocia cada persona con el conjunto de los países que ha visitado:
    paises = {
        'Pepito': {'Chile', 'Argentina'},
        'Yayita': {'Francia', 'Suiza', 'Chile'},
        'John': {'Chile', 'Italia', 'Francia', 'Peru'},
    }
    Escriba una funcion cuantos_en_comun(a, b), que indique cuántos países en común han visitado 
    la persona a y la persona b:
"""

def cuantos_en_comun(n1, n2):
    paises = {
        'Pepito': {'Chile', 'Argentina'},
        'Yayita': {'Francia', 'Suiza', 'Chile'},
        'John': {'Chile', 'Italia', 'Francia', 'Peru'},
    }

    comun = paises[n1].intersection(paises[n2])
    print("Entre {} y {} la cantida de paises en común es {}".format(n1,n2, len(comun)))

cuantos_en_comun("Pepito", "Yayita")