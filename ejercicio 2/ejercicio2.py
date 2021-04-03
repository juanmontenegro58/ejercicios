""" 
    Escribir un programa que dada dos listas devuelva una nueva llsta con los valores intercalados.
"""
def main(l1, l2):
    new_list = []
    for i, v in enumerate(l2):
        new_list.append(l1[i])
        new_list.append(v)
    print(new_list)
main(["Andres", "Carlos", "Alguien"],["Andrea", "Camila", "Johana"])