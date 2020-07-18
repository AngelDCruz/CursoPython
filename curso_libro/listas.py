
frutas = ["cereza","frambueza","coco","piña"]

# acceder a valor accediendo por su indice
print(frutas[1])

# comprobar si existe un valor en la lista con la palabra reservada in
existe_fruta = "sandia" in frutas
print("existe la sandia en la lista? {0}".format(existe_fruta))

# Modificar los valores de una lista numerica
lista_numeros =  [1, 2, 3, 4, 5]

for valor in range(len(lista_numeros)):
    
    lista_numeros[valor] = lista_numeros[valor] + 2
    
print(lista_numeros)


# concatenar dos listas
lista_concatenada = frutas + lista_numeros
print(lista_concatenada)

# multiplicar listas
generar_listas = lista_concatenada *  2
print(generar_listas)



# rebanado de listas
lista_rebanada = frutas[0:2]
print(lista_rebanada)


# METODOS DE LISTAS
lista_nombres_1 = ["juan", "pedro", "susana"]
lista_nombres_2 = ["william", "elias", "kaylani"]

# unir las dos listas en una
lista_nombres_1.extend(lista_nombres_2)
print(lista_nombres_1)

# agregar un nuevo elemento a la lista
lista_nombres_1.append("francisco")
print(lista_nombres_1)

# ordenar una lista de forma ascendente
lista_nombres_1.sort(reverse=False) # ordena de forma ascendente
print(lista_nombres_1)

# ordenar una lista de forma descendente
lista_nombres_1.sort(reverse=True)
print(lista_nombres_1)

# eliminar un elemento con pop 
# indicar el indice o sin indice elimina el ultimo elemento de la lista
lista_nombres_1.pop()
print(lista_nombres_1) # elimina el ultimo elemento de la lista
lista_nombres_1.pop(1)
print(lista_nombres_1) # elimina un elemento en base al indice que ingresemos

# si sabes el nombre del elemento de una lista puedes utilizar el metodo remove
lista_nombres_1.remove("william")
print(lista_nombres_1)

# eliminar con la palabra reservada del y usando rebanadas
del lista_nombres_1[0:2]
print(lista_nombres_1)


# FUNCIONES DE LISTAS
    # min()
    # max()
    # sum()
    # len()

lista_numeros_funciones = [1,2,3,4,5,6,7,8,9,10]

# obtener le numero mas pequeño de la lista con la funcion min(param)
numero_menor = min(lista_numeros_funciones)
print(f"el número más pequeño es:{numero_menor}")

# obtener el numero más grande de la lista con la funcion max(param)
numero_mayor = max(lista_numeros_funciones)
print(f"el número más grande es:{numero_mayor}")

# suma de todo los numero de la list con la funcion sum(param)
sumatoria_numeros = sum(lista_numeros_funciones)
print(sumatoria_numeros)

# total de elemento de una lista con la funcion len(param)
total_elementos_lista = len(lista_numeros_funciones)
print(total_elementos_lista)



# EJECICIO SACAR EL PROMEDIO MEDIANTE UN CICLO WHILE E INGRESAR NUEVOS VALORES
# EL CICLO SERA INFINITO HASTA QUE CON UN CONDICIONAL PARE LA EJECUCION Y ARROJE EL RESULTADO
contador = 0
total = 0
promedio = 0

while(True):

    try:
        
        valor = input("ingresa un numero:")

        if valor == "fin": 
            break

        total = total + float(valor)
        
        contador = contador + 1
    
    except:
        print("el valor que ingresastes no es un numero")
        exit()

# calculo de promedio
try:
    promedio = total / contador
except:
    print("el numero no puede divirse entre ceros")

print(f"El promedio es {promedio}")


# EJEMPLO DOS
# CREAR UNA LISTA VACIA QUE UTILIZE EL METODO APPEND PARA AGREGAR NUEVOS VALORES
# UTILIZANDO EL ITERADOR WHILE
contador_2 = 0
total_2 = 0
promedio_2 = 0
lista_numero_agregar = []

while(True):

    try:

        valor = input("Ingresa un número:")

        if valor == "fin": break

        valor = float(valor)

        lista_numero_agregar.append(valor)

        contador_2 = contador_2 + 1

    except:
        print("El valor que ingresastes no es un numero")

promedio_2 = sum(lista_numero_agregar) / contador_2
print(f"El promedio es:{promedio_2}")