### Tuplas -> Listas con valores inmutables (la sintaxis se diferencia de las litas porque usa parentesis() y no corchetes[] como las listas
my_t = (3,) # Para definir una tupla de un solo valor hay que utilizar la coma ','
print(my_t)

dimensions = (200, 10) # Tupla de mas de un valor, que es lo normal
print(dimensions[0]) # Imprimo el valor del primer elemento

for dimension in dimensions: # Recorro e imprimo con un bucle for los valores de la tupla
    print(dimension)

### Modificar los valores de una tupla asignando nuevos valores a la variable
dimensions = (1000, 500)
for dimension in dimensions:
    print(dimension)

### Restaurant
restaurant_dishes = ("dishe one", "dishe two", "dishe three", "dishe four", "dishe five")
for dishe in restaurant_dishes:
    print(dishe)

restaurant_dishes = ("dishe_zero", "dishe one", "dishe two")
for dishe in restaurant_dishes:
    print(dishe)