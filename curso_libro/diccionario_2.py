

# CREAR UN PROGRAMA QUE INGRESE EL NOMBRE DEL ARCHIVO
# CUENTE EL TOTAL DE LETRAS QUE SE REPITEN EN EL TEXTO 
# UTILIZAR UN DICCIONARIO

archivo = input("nombre del documento:")
diccionario_palabras = dict()

try:

    archivo_abrir = open(archivo)

    for texto in archivo_abrir:
        
        lista_palabras = texto.split()

        for letra in lista_palabras:

            if letra not in diccionario_palabras:

                diccionario_palabras[letra] = 1

            else:

                diccionario_palabras[letra] += 1


except:

    print("ingresa un nombre de documento valido")
    
print(diccionario_palabras)


# DICCIONARIOS Y BUCLES
lista_nombre = {
    "nombre":"juan",
    "apellido":"cruz",
    "edad":22
}

# hay dos formas de impirmir los valores de un diccionario
for valor in lista_nombre:
    print(lista_nombre[valor])

# imprimiendo llave valor
for indice, valor in lista_nombre.items():
    print(f"{indice} {valor}")

# imprimiendo valores
for valor in lista_nombre.values():
    print(valor)