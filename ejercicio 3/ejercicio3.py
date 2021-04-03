""" 
    Escribir un programa que gestione las facturas pendientes de cobro de un empresa. Las facturas se almacenan
    en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura.
    El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si
    desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadira al diccionario.
    Si se desea pagar una factura se preguntará por el número de factura y se eliminara del diccionario. Después
    de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad 
    pendiente de cobro.
"""

def main():
    facturas = {}
    acumulado = 0
    cobrado = 0
    bandera = True
    while bandera:
        print("-------------------------------OPCIONES--------------------------------------------")
        print("1: Añadir nueva factura")
        print("2: Pagar factura")
        print("3: ¿Terminar?\n")
        opcion = int(input(""))
        if opcion == 1:
            numero_factura = int(input("Ingresa el número de la factura: "))
            valor_factura = float(input("Ingresa el valor de la factura: "))
            facturas[numero_factura] = valor_factura
            acumulado += valor_factura
            print("Valor pendiente por pagar {}: ".format(acumulado))
        elif opcion == 2:
            numero_factura = int(input("Ingrese el número de la factura a pagar: "))
            if numero_factura in facturas.keys():
                cobrado += facturas[numero_factura]
                acumulado -= facturas[numero_factura]
                print("Valor de la factura {} \n".format(facturas[numero_factura]))
                print("Cobrado hasta ahora {} queda pendiente un saldo de {}".format(cobrado, acumulado))
                facturas.pop(numero_factura)
                print("Factura cancelada con exito ")
            else:
                print("No se encontró la factura ")
        elif opcion == 3:
            bandera = False
        else:
            print("La opcion seleccionada no esta disponible. Intente de nuevo\n")
            
if __name__ == '__main__':
    main()