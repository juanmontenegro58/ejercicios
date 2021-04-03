""" 
    Escribir un programa para gestionar una agenda telefoníca con los nombres y los telefonos de los clientes de 
    una empresa. El programa debera crear el fichero si no existe, para consultar el número de un cliente, añadir 
    el telefono de un nuevo cliente y eliminar el número de un cliente. El nombre del cliente y su telefono deben
    aparecer separados por comas y cada cliente en una linea distinta.
"""

import os

def main():
    bandera = True
    while bandera:
        print("-------------------OPCIONES-------------------------------")
        print("0: Listar Todos los clientes")
        print("1: Agregar nuevo cliente")
        print("2: Consultar cliente")
        print("3: Eliminar cliente")
        print("4: Finalizar")
        opcion = int(input(""))

        if opcion == 0:
            listar_clientes()

        elif opcion == 1:
            agregar_cliente()
        
        elif opcion == 2:
            consultar_cliente()
        
        elif opcion == 3:
            eliminar_cliente()
        
        elif opcion == 4:
            print("Finalizando ¿Desea conservar el archivo? s(si)/n(no)")
            opcion = input("")
            if opcion == 'n':
                os.remove("agenda.txt")
                print("Archivo eliminado ")
            bandera = False
        else:
            print("Opción no diaponible. Intenta de nuevo\n")

def listar_clientes():
    with open("agenda.txt", "r") as a:
        data = a.readlines()
        di = {}
        for i in data:
            di[i.split(',')[0]] = i.split(',')[1]
        
        for k, v in di.items():
            print("{} - {} ".format(k,v))

def agregar_cliente():
    nombre = input("Nombre del cliente: ")
    numero = int(input("Número de telefono: "))
    with open("agenda.txt", "a") as a:
        a.write("{},{}\n".format(nombre, numero))
    print("El cliente se agrego con exito\n")


def consultar_cliente():
    nombre = input("Ingresa el nombre del cliente: ")
    with open("agenda.txt", "r") as a:
        data = a.readlines()
        di = {}
        for i in data:
            di[i.split(',')[0]] = i.split(',')[1]
            
        if nombre in di.keys():
            print("{} - {}".format(nombre, di[nombre]))
        else:
            print("No se encontro informacion relacionada.")

def eliminar_cliente():
    nombre = input("Ingresa el nombre del cliente: ")
    with open("agenda.txt", "r") as a:
        data = a.readlines()
        di = {}
        for i in data:
            di[i.split(',')[0]] = i.split(',')[1]
            
        if nombre in di.keys():
            del di[nombre]
            print("El cliente se eliminó correctamente ")
        else:
            print("No se encontro informacion relacionada.")

    with open("agenda.txt", "w") as a:
        for k, v in di.items():
            a.write("{},{}\n".format(k,v))
            
if __name__ == '__main__':
    if os.path.exists("agenda.txt"):
        print("El archivo ya esta creado")
    else:
        file = open("agenda.txt", "w")
        file.close()
    main()