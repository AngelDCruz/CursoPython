entrada = input("ingresa un numero: ")

try:
    resultado = int(entrada) * 2
    print("el resultado de la operación es {0}".format(resultado))
except:
    print("ingrese un número valido")