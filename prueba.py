"""
En esta parte agregamos la libreria para poder hacerlo son raiz
"""
import math
def suma(a,b):
    return a + b
def resta(a,b):
    return a -b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir con 0"
def Potencia(a,b):
    return a ** b
def raiz(n):
    if n >= 0:
        return math.sqrt(n)
    else:
        return "No se puede calcular la raiz de un numero negativo"
    

#Entorno Visual para el usuario

print("Calculadora")
print(" ")
print("Operaciones:")
print("1_ Suma")
print("2_ Multiplicacion")
print("3_ Resta")
print("4_ Division")
print("5_ potencia(primer numero base, segundo el numero a elevar)")
print("6_Raiz")

opcion = input("Seleccione un numero para su operacion: ")
n1=float(input("Ingrese primer numero: "))
n2=float(input("Ingrese segundo numero: "))

if opcion == "1":
    resultado = suma(n1,n2)
    print("El resultado de la suma es:",resultado)
elif opcion == "2":
    resultado= multiplicacion(n1,n2)
    print("El resultado de la multiplicacion es",resultado)
elif opcion == "3":
    resultado= resta(n1,n2)
    print("El resultado de la resta es",resultado)
elif opcion == "4":
    resultado= division(n1,n2)
    print("El resultado de la division es",resultado)
elif opcion == "5":
    
    resultado= Potencia(n1,n2)
    print("El resultado de la potencia es:",resultado)
elif opcion == "6":

    resultado= raiz(n1)
    resultado2 = raiz(n2)
    print("La raiz cuadradada  de tu primer  numero es ",resultado)
    print("La raiz cuadrada de tu segundo numero es",resultado2)
    
else:
    print("Opcion no valida. Intente de vuelta")
