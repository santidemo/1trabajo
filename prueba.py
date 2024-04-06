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
    

#Entorno Visual para el usuario

print("Calculadora")
print(" ")
print("Operaciones:")
print("1_ Suma")
print("2_ Multiplicacion")
print("3_ Resta")
print("4_ Division")
