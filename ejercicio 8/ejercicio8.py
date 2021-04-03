""" 
    Las notas de un ramo están almacenadas en un archivo llamado notas.txt, que contiene lo siguiente:
    Pepito:5.3:3.7:6.7:6.7:7.1:5.5
    Yayita:5.5:5.2:2.0:5.6:6.0:2.0
    Fulanita:7.1:6.6:6.4:5.1:5.8:6.3
    Moya:5.2:4.7:1.8:3.5:2.7:4.5
    Cada línea tiene el nombre del alumno y sus seis notas, separadas por dos puntos (”:”).
    Escriba un programa que cree un nuevo archivo llamado reporte.txt, en que cada línea indique
    si el alumno está aprobado (promedio ≥ 4,0) o reprobado (promedio < 4,0):
"""

def main():
    with open("notas.txt", "r") as file:
        dic = {}
        final = {}
        data = file.readlines()
        for i in data:
            dic[i.split(":")[0]] = i.strip().split(":")[1:]

        for k, v in dic.items():
            total = 0
            for i in v:
                total += float(i)
            final[k] = total / len(v)
    with open("reporte.txt", "w") as file:
        for k, v in final.items():
            if v > 4.0:
                file.write("{} Aprobado\n".format(k))
            else:
                file.write("{} Reprobado\n".format(k))
    print("Guardado en reporte.txt")
        
if __name__ == '__main__':
    main()