#hola mundo
print("hola mundo")

print(10+5)

print(10-5)

print(10*5)

print(10/5)

#funcion de redondeo
print(round(10/5))

num1=10
num2=5

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1**num2)

numero = 20 #variable
print(numero == 20)
print(numero == 20)
print(numero == 20)

nombre = "Emiliano"
apellido = "Brizuela"

nombreCompleto = nombre + " " + apellido
#formato de como escribir una funcion la f cambia la sintaxis para que sea mas sensillas (a ver)
nombre = f'{nombre} {apellido}'
print(nombreCompleto, nombre)

#ejemplo de if, else, elif

edad = 17
compleanios = True

if(edad >= 18):
    print("eres mayor de edad")
    if(compleanios):
        print("Feliz cumple")
elif((edad >= 13) and (edad < 18)):
    print("eres un adolescente")
else:
    print("eres menor de edad")