# Solicitar al usuario una contraseña
contrasena = input("Ingresa una contraseña: ")

# Comprobar si la contraseña cumple los requisitos
tiene_mayuscula = any(char.isupper() for char in contrasena)
tiene_minuscula = any(char.islower() for char in contrasena)
tiene_numero = any(char.isdigit() for char in contrasena)
tiene_longitud_valida = len(contrasena) >= 8

# Imprimir un mensaje indicando si la contraseña es válida o no
if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_longitud_valida:
    print("La contraseña es válida.")
else:
    print("La contraseña no cumple con los requisitos.")