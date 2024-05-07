tieneMasBultos = True
nroBulto = 1
valorPagarPorKilo = 0
valorPesoLiviano = 1000
valorPesoNormal = 4500
totalLiviano = 0
totalNormal = 0
contadorBultosLivianos = 0
contadorBultosNormales = 0

cantidadBultos = int(input("Ingrese cantidad de bultos: "))
for i in range(cantidadBultos):
    try:
        pesoBulto = int(input(f"Ingrese el peso (1 a 10kg) del bulto Nro. {nroBulto}: "))
    except ValueError:
        print("Peso del bulto debe estar en el rango de 1 y 10kg.")
        continue

    if 1 <= pesoBulto <= 5:
        totalLiviano += valorPesoLiviano
        contadorBultosLivianos += 1
    elif 6 <= pesoBulto <= 10:
        totalNormal += valorPesoNormal
        contadorBultosNormales += 1
    else:
        print("Peso ingresado incorrecto (1 - 10kg)")

    nroBulto += 1

print(f"Total a pagar por bultos livianos: {totalLiviano}")
print(f"Total a pagar por bultos normales: {totalNormal}")
print(f"Cantidad de bultos livianos: {contadorBultosLivianos}")
print(f"Cantidad de bultos normales: {contadorBultosNormales}")