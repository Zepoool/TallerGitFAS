"""
Proyecto: Taller Git y GitHub
Equipo: Equipo FAS
Descripción: Programa de operaciones matemáticas simples en Python.
"""

"""
Funciones básicas
"""
# Definimos las funciones
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b
  
def division(a, b):
    return a / b

# Bloque principal
if __name__ == "__main__":
 
# Programa principal
    print("=== Calculadora de operaciones básicas matemáticas ===")
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

print("La suma es:", sumar(a, b))
print("La resta es:", restar(a, b))
print("La multiplicación es:", multiplicacion(a,b))
print("La división es:", division(a, b))
