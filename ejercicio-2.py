class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def comer(self):
        return "Estoy comiendo"


class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza

    def correr(self):
        return "Estoy corriendo"


class Aguila(Animal):
    def volar(self):
        return "Estoy volando"


animal = Animal(cantidad_patas=4, tipo="vertebrado")


perro = Perro(cantidad_patas=4, tipo="vertebrado", nombre="Firulais", raza="Labrador")


aguila = Aguila(cantidad_patas=2, tipo="vertebrado", )


print("Atributos del animal:")
print("Cantidad de patas:", animal.cantidad_patas)
print("Tipo:", animal.tipo)

print("\nAtributos del perro:")
print("Cantidad de patas:", perro.cantidad_patas)
print("Tipo:", perro.tipo)
print("Nombre:", perro.nombre)
print("Raza:", perro.raza)

print("\nAtributos del águila:")
print("Cantidad de patas:", aguila.cantidad_patas)
print("Tipo:", aguila.tipo)


print("\nComportamiento del animal:")
print(animal.comer())

print("\nComportamiento del perro:")
print(perro.comer())
print(perro.correr())

print("\nComportamiento del águila:")
print(aguila.comer())
print(aguila.volar())
