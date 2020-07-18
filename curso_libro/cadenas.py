
fruta = "manzana"

# recorriendo fruta por el indice 
contador = 0

for valor in fruta:

    caracter = fruta[contador]

    print(caracter)

    contador = contador + 1


contador_2 = 0

while contador_2 < len(fruta):

    caracter = fruta[contador_2]

    print(caracter)

    contador_2 = contador_2 + 1


# REBANADO DE UN CARACTER
rebanar_caracter = "quiero que me rebanes"
print(rebanar_caracter[0:6])   


# OPERADOR IN
resultado_in = "quiero" in rebanar_caracter
print(resultado_in)