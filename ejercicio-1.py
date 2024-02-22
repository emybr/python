def accion_A(a, b):
    return a + b

def accion_B(a, b):
    return a * b

def main():
    while True:
        opcion = input("Ingrese 1 para sumar o 2 para multiplicar. ")
        
        if opcion in ('1', '2'):
            opcion = int(opcion)
            
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if opcion == 1:
                resultado = accion_A(num1, num2)
                print("El resultado de la acción A es:", resultado)
            else:
                resultado = accion_B(num1, num2)
                print("El resultado de la acción B es:", resultado)
                
            break 
        else:
            print("Opción no válida. Por favor, ingrese 1 o 2.")


if __name__ == "__main__":

    main()