
sets = {
     "uva",
     "fresa",
     "durazno"
}

sets_2 = {
    "melocoton",
    "coco",
    "piña"
}

# metodos disponibles
print(dir(sets))

# agrega un nuevo valor al sets
sets.add("pera")
print(sets)

# agrega multiples valores al set
sets.update(["sandia", "manzana", "naranja"])

# remueve un elemento mediante el valor
sets.remove("fresa")
print(sets)

# borra un elemento del set
sets.discard("sandia")
print(sets)

# remueve el ultimo elemento del set
sets.pop()
print(sets)

# une dos sets en uno solo
sets_3 = sets.union(sets_2)
print(sets_3)

# borrar elementos del sets
sets.clear()
print(sets)

# borrar variable con asignacion
#del sets
print(sets)

# tambien se puede usar el constructor para construir un conjunto tipo set
constructor_set = set(("piña", "cereza", "pitaya"))
print(constructor_set)
