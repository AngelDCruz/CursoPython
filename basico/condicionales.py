
numero_1 = 10
numero_2 = 20
color = "verde"

if(numero_1 > numero_2):
    print(f"el numero {numero_1} es mayor a {numero_2}")
else:
    print(f"el numero {numero_2} es mayor a {numero_1}")

if(color == "naranja"):
    print("el color es naranja")
elif(color == "verde"):
    print("el color es verde")
else:
    print("no se asigno ningun color")

# operadores logicos
#and
if(numero_1 <= 10 and numero_1 > -1):
    print("el numero es posivo")
else:
    print("el numero es negativo")
#or
if(numero_1 == 10 or numero_1 == 2):
    print("el numero es un par")
else:
    print("el numero es impar")
#not
if(not(numero_1 == 10)):
    print("el numero no es 10")
else:
    print("el numero es 10")

