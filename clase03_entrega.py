nombres = [["Juan", "Maria"], "Juan", "Maria"]
edades = [10, 15, 20]

print(nombres[0])
print(edades)

# append - agrega un elmento a la lista

nombres.append("Pedro")
print(nombres)

# extend - agrega una lista a la lista
mas_nombres = ["Emy", "Carlos"]
nombres.extend(mas_nombres)
print(nombres)
nombres.extend(["Luis", "Carlos"])
print(nombres)

# insert - inserta un elemento en una posicion determinada

nombres.insert(0, "Pedro")
print(nombres)

# remove - elimina un elemento de la lista

nombres.remove("Pedro")
print(nombres)

#pop - elimina un elemento de la lista y lo devuelve
# pop() - elimina el ultimo elemento    
# pop(0) - elimina el primer elemento

nombres.pop(0)
print(nombres)

numero = [1, 2, 4, 3, 5, 6, 8, 7, 9, 10]

print(numero)

# sort - ordena los elementos de la lista

numero.sort()
print(numero)

# reverse - invierte los elementos de la lista

numero.reverse()
print(numero)


# Tuplas - listas que no se pueden modificar

tupla = ("Lunes",
        "Martes",
        "Miercoles",
        "Jueves",
        "Viernes",
        "Sabado",
        "Domingo")
print(tupla)

# cout - cuenta los elementos de la lista

print(len(tupla))
print(tupla.count("Lunes"))

# index - devuelve el indice de la lista

print(tupla.index("Lunes"))

# entidad (tiene sus caracteristicas )

persona = {
    "nombre": "Juan",
    "apellidos": "Perez",
    "edad": 20
}

print(persona)
print(persona.keys())

# value - devuelve los valores de la lista
print("value",persona.values())
# item - devuelve los items de la lista
print("item",persona.items())
# get - devuelve un elemento de la lista
print("get",persona.get("nombre"))

print(persona["nombre"])

#eliminar un elemento

persona.pop("apellidos")
print("pop",persona)

# clear - elimina todos los elementos de la lista

persona.clear()
print("clear",persona)

# ciclo for

for nombre in nombres:
    print("Hola", nombre)

for e in tupla:
    print(e)

# for anidado
for nombre in nombres:
    print("Hola", nombre)
    for e in tupla:
        print(e)

#funciones nativas de python

print("hola mundo")


# funcion definida por el usuario 
precio = 2500

def suma_iva(precio=0):
    precio_con_iva = precio * 1.21  # Asumiendo una tasa de IVA del 16%
    return precio_con_iva

print(suma_iva())  # Llamada a la función sin argumentos, utilizará el valor predeterminado 0
print(suma_iva(200))  # Llamada a la función con un argumento
