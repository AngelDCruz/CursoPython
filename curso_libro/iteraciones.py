
# ITERACIONES

# while
iteracion = 5

while(iteracion > 0):
    iteracion = iteracion - 1
    print("despegando")

# BUCLES INFINITOS BREAK Y CONTINUE
while(True):
    
    entrada = input("ingresa tu nombre")
    
    if(entrada == "fin" or entrada == "exit"):
        break

while(True):

    entrada = input("ingresa texto:")

    if(entrada[0] == "#"):
        continue

    if(entrada == "fin" or entrada == "exit"):
        break

    print("texto de entrada {0}".format(entrada))



# BUCLE FOR
nombre_a_imprimir = ["rey", "rosa", "wili"]

for valor in nombre_a_imprimir:
    print(valor)


# contar el numero de elemento de un lista no usando len()
contador = 0
for valor in nombre_a_imprimir:
    contador = contador + 1
print("numero de elementos: {0}".format(contador))

# suma de elementos de una lista que contiene numeros
lista_numeros = [1, 5, 10, 5]
total_suma_numeros = sum(lista_numeros)
total_elementos_numeros = len(lista_numeros)
print(total_suma_numeros)
print(total_elementos_numeros)

