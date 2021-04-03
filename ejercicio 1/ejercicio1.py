""" 
    Escribir un programa que almacene las asignaturas de un curso (Matemáticas, Física, Química, Historia y lengua)
    en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
    aprobadas. Al final el programa debe mostrar pon pantalla las asignaturas que el usuario tiene que repertir
"""
def main():
    asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'lengua']
    temp = []
    for i in asignaturas:
        nota = float(input("Ingresa la nota de la materia {}: ".format(i)))
        if nota >= 3.5:
            temp.append(i)
    
    if len(temp) == len(asignaturas):
        print("No tienes asignaturas por repetir")
    else:
        for i in temp:
            asignaturas.remove(i)
        print("Debes repetir las siguientes asignaturas {} ".format(asignaturas))
    
if __name__ == '__main__':
    main()