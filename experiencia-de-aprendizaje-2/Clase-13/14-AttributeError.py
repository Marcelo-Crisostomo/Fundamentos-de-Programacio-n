try:
    my_list = [1, 2, 3]
    my_list.append_item(4)
except AttributeError:
    print("Error: Atributo o método no encontrado.")