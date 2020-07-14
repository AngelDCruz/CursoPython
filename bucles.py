
lista = [1, "nombre", True]
tupla = ("roxana","mendez", True)
diccionario = {
    "nombre": "susana",
    "apellido": "arias"
}

# recorrer una lista
for valor in lista:
    print(f"imprimiendo valor de lista:{valor}")

# recorrer una tupla
for valor in tupla:
    print(f"imprimiedo valor de tupla:{valor}")

# recorrer diccionario
for valor in diccionario.values():
    print(f"imprimiendo valor de diccionario:{valor}")

# recorrer diccionario con llave y valor
for llave, valor in diccionario.items():
    print(f"llave:{llave} y valor:{valor} del diccionario")


# imprimir numeros del 1 al 10 con while
contador = 0

while contador <= 10:
    if contador != 0: print(contador) 
    contador = contador + 1