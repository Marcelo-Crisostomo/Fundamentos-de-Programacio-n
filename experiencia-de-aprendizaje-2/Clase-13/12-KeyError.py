try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
except KeyError:
    print("Error: Clave no encontrada en el diccionario.")