
nombre_archivo = input("ingresa el nombre del archivo y su extencion:")
contador = 0

try:
    archivo_abierto = open(nombre_archivo)
except:
    print(f"el nombre de archivo no es valido {nombre_archivo}")
    exit()

for valor in archivo_abierto:

    valor = valor.rstrip()

    if valor.startswith("From:"):
        print(valor)
