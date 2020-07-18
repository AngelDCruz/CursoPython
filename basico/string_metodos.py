
saludo = "Hola mundo"
pensamiento = "La vida es bella"

# convierte a minuscula
saludoMinusculas = saludo.lower()
print(saludoMinusculas)

# convierte a mayusculas
saludoMayusculas = saludo.upper()
print(saludoMayusculas)

# capitaliza la primer letra de cadena a mayuscula
saludoCapitaliza = saludo.capitalize()
print(saludoCapitaliza)

# remplaza una letra o texto si se encuentra en una cadena por otra
saludoReemplaza = saludo.replace("Hola", "Bienvenidos hola")
print(saludoReemplaza)

# cuenta cuantos caracteres encuentra dependiendo la busqueda
saludoContadorCaracteres = saludo.count("o")
print(saludoContadorCaracteres)

# devuelve un true o false si encuentra una coincidencia al inicio de una cadena de texto
saludoIniciaCon = saludo.startswith("he")
print("Hola mundo inicia con he?", saludoIniciaCon)

# devuelve un true o false si encuentra una coincidencia al final de una cadena de texto
saludoFinCon = saludo.endswith("do")
print("Hola mundo termina con do?", saludoFinCon)

# particiona una cadena de texto en una lista
saludoLista = saludo.split(" ")
print(saludoLista)

# encuentra la posicion de la primer letra o frase
saludoEncuentraPosicion = saludo.find("m")
print("posición en que se encuentra la letra m:", saludoEncuentraPosicion)

# encuentra el indice de la primer letra o frase 
saludoEncuentraIndice = saludo.index("m")
print("posición en que se encuentra la letra m:", saludoEncuentraIndice)

# cuenta la cantidad de caracteres que tiene almacenado una cadena
saludoCuentaCaracteres = len(saludo)
print("número de carácteres:",saludoCuentaCaracteres)

# comprueba si un dato o cadena es numerico o no, devuelve un true o false
saludoEsNumerico = saludo.isnumeric()
print("La cadena es un dato numerico?",saludoEsNumerico)

# comprueba si un dato o cadena es alfanúmerico o no, devuelve un true o false
saludoEsAlfanumerico = saludo.isalpha()
print("La cadena es un dato alfanúmerico?",saludoEsAlfanumerico)

# devuelve una letra dependiendo la posicion que indexemos
print("La letra que devuelve la posición es:",saludo[2])

# unir cadena de textos con variables
print(f"{saludo}, como estas?")
print("{0}, como estas?, {1}".format(saludo, pensamiento))