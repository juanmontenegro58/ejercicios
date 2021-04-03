""" 
    La asistencia de los alumnos a clases puede ser llevada en una tabla, En un programa, esta informacion puede ser 
    representada usando listas:
    alumnos = ['Pepito', 'Yayita', 'Fulanita', 'Panchito']
    asistencia = [
        [True, True, True, False, False, False, False],
        [True, True, True, False, True,  False, True ],
        [True, True, True, True,  True,  True,  True ],
        [True, True, True, False, True,  True,  True ]]
    1. Escriba la función total_por_alumno(tabla) que reciba como parámetro la tabla de asistencia y retorne una lista 
    con el número de clases a las que asistió cada alumno.
    2. Escriba la función total_por_clase(tabla) que reciba como parámetro la tabla de asistencia y retorne una lista 
    con el número de alumnos que asistió a cada clase.
    3.Escriba la función alumno_estrella(asistencia) que indique qué alumno asistió más a clases.
    4.Agregue un decorador que diga cuanto se tardo la ejecucion.

"""

import time

def decorador(funcion):
    def medir_tiempo(*args, **kwargs):
        inicio = time.time()
        funcion(*args, **kwargs)
        fin = time.time()
        print("Ejecución de la funcion {} finalizada en {} \n".format(funcion.__name__,fin-inicio))
    return medir_tiempo

@decorador
def total_por_alumno(tabla):
    nueva_lista = []
    for i in tabla:
        asistencia = 0
        for j in i:
            if j:
                asistencia += 1
        nueva_lista.append(asistencia)
    print(nueva_lista)

@decorador
def total_por_clase(tabla):
    nueva_lista = []
    for i in range(len(tabla[0])):
        con = 0
        for j in range(len(tabla)):
            if tabla[j][i] == True:
                con += 1
        nueva_lista.append(con)
    print(nueva_lista)
    
@decorador
def alumno_estrella(alumnos,tabla):
    alumno_estrella = ''
    for k,i in enumerate(tabla):
        asistencia = 0
        for j in i:
            if j:
                asistencia += 1
                if asistencia == len(i):
                    alumno_estrella = alumnos[k]
    if not alumno_estrella:
        print("No hay alumno extrella. ")
    print(alumno_estrella)

alumnos = ['Pepito', 'Yayita', 'Fulanita', 'Panchito'] 
asistencia = [
        [True, True, True, False, False, False, False],
        [True, True, True, False, True,  False, True ],
        [True, True, True, True,  True,  True,  True ],
        [True, True, True, False, True,  True,  True ]
    ]
total_por_alumno(asistencia)
total_por_clase(asistencia)
alumno_estrella(alumnos, asistencia)