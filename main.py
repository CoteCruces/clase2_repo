
print("Calculadora")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")

while True:
    opcion = int(input("Ingrese la opcion: "))
    num1 = int(input("Ingrese numero 1: "))
    num2 = int(input("Ingrese numero 2: "))
    if opcion == 1:
        resultado = num1 + num2
        print(f"El resultado es {resultado}")
    
    elif opcion == 2:
        resultado = num1 - num2
        print(f"El resultado es {resultado}")
        
    elif opcion == 3:
        resultado = num1 * num2
        print(f"El resultado es {resultado}")
        
    elif opcion == 4:
        print ("No se puede dividir por cero")
    
    elif opcion == 5:
        break
print("Gracias")