
# HERENCIA
from poo import Animal

class Perro(Animal):

    dueno = ""

    def datos(self):
        print(f"mi nombre es {self.dueno} y mi perro {self.nombre} es muy divertido")


perro = Perro("Firulais")
perro.dueno = "Fernando"
perro.mostrar_nombre()
perro.datos()

# usar el constructor padre
class Gato(Animal):

    dueno = ""

    def __init__(self, dueno, mascota):
        self.dueno = dueno
        Animal.__init__(self, mascota)

    def datos_descriptivos(self):
        print(f"mi nombre es {self.dueno} y mi mascota es {self.nombre}")

gato = Gato("Susana", "Garfield")
gato.datos_descriptivos()