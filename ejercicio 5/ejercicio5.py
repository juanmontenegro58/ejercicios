""" 
    Escribir una función que reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro
    diccionario con las asignaturas en mayusculas y las calificaciones en letras.
"""
def main(data):
    new_dict = {}
    for k , v in data.items():
        letra = ''
        if v < 3:
            letra = 'I'
        elif v >= 3 and v < 4:
            letra = 'A'
        elif v >= 4 and v <= 4.5:
            letra = "S"
        elif v >= 4.5 and v <= 5:
            letra = 'E'

        new_dict[k.upper()] = letra

    print(new_dict)
    return new_dict

main({"matemáticas": 4.0, "español": 3.0, "fisíca": 3.7, "historia": 4.2, "biologia": 5.0})