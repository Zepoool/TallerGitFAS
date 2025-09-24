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

# Programa principal
print("=== Calculadora de Suma y Resta ===")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

print("La suma es:", sumar(a, b))
print("La resta es:", restar(a, b))

