
# Listas y cadenas

# convertir una cadena en una lista de caracteres
nombre = "Angel Reynaldo Ortiz De La Cruz"
cadena_caracteres = list(nombre)
print(cadena_caracteres)

# dividir texto en forma de lista mediante un limitador, por defecto split delimita por un espacio en blanco
lista_cadena = nombre.split()
print(lista_cadena)

# join une las posiciones de toda la lista en una cadena de texto 
saludo = ["hola", "como", "estas", "susuana"]
unir_saludo = " "
unir_saludo = unir_saludo.join(saludo)
print(unir_saludo)