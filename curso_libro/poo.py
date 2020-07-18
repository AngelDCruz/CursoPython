
# definiendo un objeto
class Persona:
    
    nombre = "Samanta"
    apellido = "Perez"

    def mostrar_nombre(self):
        print(f"mi nombre completo es {self.nombre} {self.apellido}")


# persona = Persona()
# persona.mostrar_nombre()


class Animal:
    
    nombre = ""
    
    def __init__(self, nombre): # constructor
        print("estoy contruyendo")
        self.nombre = nombre
        
    def mostrar_nombre(self): # funcion
        print("mostrando nombre", self.nombre)
        
    #def __del__(self): # destructor
     #   print("estoy destruyendo", self.nombre)
        

# animal = Animal()
# animal.mostrar_nombre()


# PARAMETRIZANDO CONSTRUCTOR
class Carro:

    modelo = ""

    def __init__(self, modelo):
        self.modelo = modelo

    def mostrar_nombre_modelo(self):
        print(f"el modelo del auto es {self.modelo}")

# honda = Carro("Honda")
# honda.mostrar_nombre_modelo()