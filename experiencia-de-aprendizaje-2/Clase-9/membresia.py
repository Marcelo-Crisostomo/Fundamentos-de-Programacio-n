# Solicitar al usuario que ingrese el tipo de membresía
membresia = input("Ingrese su tipo de membresía (básica/premium/vip): ")

# Verificar los beneficios de la membresía
if membresia.lower() == "premium" or membresia.lower() == "vip":
    # Si la membresía es "premium" o "vip", se otorgan beneficios adicionales
    print("Usted tiene acceso a beneficios adicionales:")
    print("- Descuento del 20% en todas las compras")
    print("- Envío gratuito en pedidos superiores a $100")
    if membresia.lower() == "vip":
        # Si la membresía es "vip", se otorga un beneficio exclusivo adicional
        print("- Acceso a eventos exclusivos para miembros VIP")
else:
    # Si la membresía es "básica" o cualquier otro valor, no se otorgan beneficios adicionales
    print("Usted tiene una membresía básica. No hay beneficios adicionales disponibles.")