
# ANALIZANDO LINEAS

# busqueda de dia en parrafo que empieze por From del archivo
try:

    archivo = open("texto.txt")

    for valor in archivo:

        valor = valor.rstrip()

        if valor.startswith("From "):

            valor_arreglo = valor.split(" ")

            dia_ingles = valor_arreglo[2]

            print(dia_ingles)
except:
    print("el documento no se puedo abrir correctamente")

print("----------------------------------")

# comprobar si dos objetos son idendicos
a = "banana"
b = "banana"
c = ["sandia", "banana"]

print(a is b) # a y b son objetos identicos
print(a is c) # a y c no son objetos identicos


# eliminar un numero de una lista
lista_numeros = [2, 8, 4]
del lista_numeros[1]
print(lista_numeros)