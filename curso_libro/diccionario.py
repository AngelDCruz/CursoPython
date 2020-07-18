
# DICCIONARIO

# crear un diccionario
crear_diccionario = dict()
print(crear_diccionario) # imprime un diccionario vacio

# agregar elementos a un diccionario
crear_diccionario["nombre"] = "angel"
print(crear_diccionario)

# acceder a el valor de un elemento
print(crear_diccionario["nombre"])

# cuenta numero de elementos en el diccionario
total_elementos = len(crear_diccionario)
print(total_elementos)

# verifica si existe una clave con el valor indicado
print("apellido" in crear_diccionario)


# crear una lista si el objeto es un diccionario
lista_valores = list(crear_diccionario.values())
print("rey" in lista_valores)


# EJERCICIO 
# contar cuantas veces se repiten las letras en un diccionario y crear sus respectivos indices valor
frase = "La vida es bella"
diccionario_caracter = dict()

for letra in frase:

    if letra not in diccionario_caracter:
        diccionario_caracter[letra] = 1
    else:
        diccionario_caracter[letra] = diccionario_caracter[letra] + 1

print(diccionario_caracter)

diccionario_caracter_2 = dict()
for letra in frase:
    diccionario_caracter_2[letra] = diccionario_caracter_2.get(letra, 0) + 1
print(diccionario_caracter_2)

    

# obtener el valor del diccionario utilizando el metodo get()
diccionario = {
    "nombre":"angel",
    "apellido":"cruz",
    "edad":26
}
obtener_valor = diccionario.get("nombre") 
print(obtener_valor)