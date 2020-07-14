
# dir nos ayuda a saber que metodos estas disponibles para una variable
# ejemplo dir("hola mundo")
# ejemplo dir([0, True, "solin"])

# Forma que se declaran las listas

lista = [0, "hola", True, [1, "mundo", False]]
lista_tupla = list((1,2,3,5))
colores = ["rojo","amarillo","verde"]
colores_ordenar = ["rojo","amarillo","verde"]

print(lista)
print(lista_tupla)

# con dir() podemos ver los metodos disponibles para un lista
#print(dir(lista))

# crear una lista mediante un rango
lista_rango = list(range(0, 10))
print(lista_rango)

# contar cuantos elementos hay en un lista
total_lista = len(lista)
print(f"total de elementos en la lista {total_lista}")

# insertar elementos tipo lista o tupla en una lista
    #insertar colores.insert(len(colores), ["azul","cafe"])
colores.insert(len(colores), ("azul","cafe"))
print(colores)

# agregar mas elementos que no sean una lista ni un tupla
colores.extend(("melon", "naranja"))
colores.extend(["zapote", "rosado"])
print(colores)

# agregar un valor nuevo a una lista
colores.append("negro")
print(colores)

# eliminar el ultimo elemento de una lista
colores.pop()
print(colores)

# eliminar un elemento dependiendo el indice o index
colores.pop(1)
print(colores)

# eliminar por el valor de una lista
colores.remove("rojo")
print(colores)

# ordenar una lista de forma ascendente sort(reverse=False)
colores_ordenar.sort(reverse=False)
print(colores_ordenar)

# ordenar una lista de forma descendente sort(reverse=True)
colores_ordenar.sort(reverse=True)
print(colores_ordenar)
colores_ordenar.reverse()
print(colores_ordenar)
