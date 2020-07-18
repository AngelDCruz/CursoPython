
# FUNCIONES DE CONVERSION DE TIPOS
# funcion min y max
cadena = "hola mundo"
numero_1 = "10"
numero_2 = 12.2

print(min(cadena)) # el caracter mas pequeño es el espacio en blanco
print(max(cadena)) # el caracter maximo es la letra u

# elimina espacio del lado derecho
print(cadena.rstrip)

# elimina espacio del lado izquierdo
print(cadena.lstrip)

# elimina espacio en blanco al principio y al final
print(cadena.strip)

# total de letras o caracteres en una frase
print(len(cadena))

# int convierte una cadena de texto numerico a un entero
conversion_numero = int(numero_1)
print(conversion_numero)

# float convierte un numero a flotante

# str convierte un dato numerico a cadena de texto
conversion_cadena = str(numero_1)
print(conversion_cadena)

conversion_flotante = float(numero_1)
print(conversion_flotante)


# FUNCIONES MATEMATICAS
import math

# obtiene el pi
pi = math.pi
print(pi)

# raiz cuadrada de un numero
raiz_cuadrada = math.sqrt(9)
print(raiz_cuadrada)

# exponte
numero_exponente = math.pow(2, 4)
print(numero_exponente)

# NUMEROS ALEATORIOS
import random

for i in range(10):
    x = random.random()
    print(x)

# obtiene un numero aleatori entre el rango fijado
numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)

# otra forma de crear numero aleatorios es creando una lista y usando el metodo choice del modulo math
numero_aleatorio_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numero_aleatorio_choice = random.choice(numero_aleatorio_lista)
print(numero_aleatorio_choice)



# DEFINICION BASICA DE FUNCIONES
def mostrar_texto():
    print("hola mundo")

def mostrar_numero(numero):
    return numero * 2

mostrar_texto()
print(mostrar_numero(2))
