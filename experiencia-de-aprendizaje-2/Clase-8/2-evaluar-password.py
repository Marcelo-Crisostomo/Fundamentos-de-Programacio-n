# Solicitar al usuario que ingrese su nombre de usuario y contraseña
usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")

# Verificar si el usuario y la contraseña son válidos
if (usuario == "pedro" and contraseña == "1234") or (usuario == "angel" and contraseña == "a4s1"):
    print("Inicio de sesión exitoso.")
else:
    print("Nombre de usuario o contraseña incorrectos.")