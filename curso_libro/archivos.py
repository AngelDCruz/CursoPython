
# para abrir un archivo lo hacemos atraves del metodo open
archivo_texto = open("texto.txt")
archivo_texto_2 = open("texto.txt")
archivo_texto_3 = open("texto.txt")
archivo_texto_4 = open("texto.txt")


leer_informacion = archivo_texto.read() # el metodo read lee la informacion que hay en el documento de texto
#print(leer_informacion)

# contar cuantos caracteres existen en el documento de texto
total_caracteres_texto = len(leer_informacion)
print(f"total de caracteres del documento {total_caracteres_texto}")


# realizar una busqueda por el metodo startswith
for valor in archivo_texto_3:

    valor = valor.rstrip() # elimina el espacio del lado derecho

    if valor.startswith('From:'):
        print(valor)

print("-----------------------------------------------------------")

# si no contiene al inicio de la busqueda que continue el proceso
for valor in archivo_texto_2:

    valor = valor.rstrip()

    if not valor.startswith("From:"):
        continue

    print(valor)

print("-----------------------------------------------------------")

for valor in archivo_texto_4:

    valor = valor.rstrip()

    if valor.find("@uct.ac.za") == -1:
        continue

    print(valor)

print("-----------------------------------------------------------")

# contar cuantas veces existe la palabra Subject en el archivo

nombre_archivo = input("ingresa el nombre del archivo")
archivo_texto_5 = open(nombre_archivo)
contador = 0

for valor in archivo_texto_5:

    valor = valor.rstrip()

    if(valor.startswith("Subject:")):
        contador = contador + 1

print("El asunto en el archivo se encuentra {0} veces".format(contador))

