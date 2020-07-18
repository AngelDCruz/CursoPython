
# declarar una funcion
def suma(num1, num2):
    return num1 + num2

print(suma(10, 15))

# funcion con parametros opcionales
def saludo(nombre="desconocido"):
    print(f"hola como estas {nombre}?")

saludo()
saludo("Fernanda")

# definir una funcion con expresion lamba
multiplicar = lambda num1, num2: num1 * num2
print(multiplicar(10, 2))