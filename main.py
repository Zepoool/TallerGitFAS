"""
Proyecto: Taller Git y GitHub
Equipo: Equipo FAS
Descripción: Programa de operaciones matemáticas simples en Python.
"""

"""
Funciones básicas
"""
# Definimos las funciones
def sumar(primerNumero, segundoNumero):
    return primerNumero + segundoNumero

def restar(primerNumero, segundoNumero):
    return primerNumero - segundoNumero

def multiplicacion(primerNumero, segundoNumero):
    return primerNumero * segundoNumero
  
def division(primerNumero, segundoNumero):
    if segundoNumero == 0:
        return "Error: No se puede dividir entre cero"
    return primerNumero / segundoNumero

# Bloque principal
if __name__ == "__main__":
    # Programa principal
    print("=== Calculadora de operaciones básicas matemáticas ===")
    primerNumero = int(input("Ingrese el primer número: "))
    segundoNumero = int(input("Ingrese el segundo número: "))

    print("La suma es:", sumar(primerNumero, segundoNumero))
    print("La resta es:", restar(primerNumero, segundoNumero))
    print("La multiplicación es:", multiplicacion(primerNumero, segundoNumero))
    print("La división es:", division(primerNumero, segundoNumero))