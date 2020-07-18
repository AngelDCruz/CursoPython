
diccionario = {
    "nombre": "angel",
    "producto": "coca cola",
    "precio": 38
}

# obtener el valor de un diccionario
valor_1 = diccionario["nombre"]
print(valor_1)
valor_2 = diccionario.get("producto")
print(valor_2)

# obtener llaves
llaves = diccionario.keys()
print(llaves)

# obtiene sus valores en tuplas dentro de una lista
print(diccionario.items())

#agregar una nueva propiedad al diccionario
diccionario["caducado"] = True
print(diccionario)

# agrega una nueva llave al diccionario con su respectivo valor
diccionario.update({ "vendido": False })
print(diccionario)

# modicar el valor de la propiedad de un diccionario
diccionario["nombre"] = "angel ortiz"
print(diccionario)

# remueve un elemento especificando la llave
diccionario.pop("caducado")
print(diccionario)

# remueve el ultimo elemento 
diccionario.popitem()
print(diccionario)

# limpia el diccionario de todos los valores existentes hasta dejarlo vacio
# diccionario.clear()
print(diccionario)


# otra forma de crear un diccionario
diccionario_constructor = dict(nombre="juan medina", edad=43)
print(diccionario_constructor)