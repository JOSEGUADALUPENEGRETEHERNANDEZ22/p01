#!/usr/bin/env python3
"""
P01 - Python Fundamentals for ISC
Proyecto de Fundamentos de Python para ISC

Este programa demuestra conceptos básicos de programación en Python:
- Variables y tipos de datos
- Operaciones básicas
- Estructuras de control
- Funciones
- Entrada y salida de datos
"""

def mostrar_tipos_datos():
    """Demuestra los tipos de datos básicos en Python"""
    print("=== TIPOS DE DATOS BÁSICOS ===")
    
    # Números enteros
    numero_entero = 42
    print(f"Número entero: {numero_entero} (tipo: {type(numero_entero).__name__})")
    
    # Números decimales
    numero_decimal = 3.14159
    print(f"Número decimal: {numero_decimal} (tipo: {type(numero_decimal).__name__})")
    
    # Cadenas de texto
    texto = "Hola, ISC!"
    print(f"Texto: {texto} (tipo: {type(texto).__name__})")
    
    # Booleanos
    verdadero = True
    falso = False
    print(f"Booleano verdadero: {verdadero} (tipo: {type(verdadero).__name__})")
    print(f"Booleano falso: {falso} (tipo: {type(falso).__name__})")
    
    # Listas
    lista_numeros = [1, 2, 3, 4, 5]
    print(f"Lista: {lista_numeros} (tipo: {type(lista_numeros).__name__})")
    
    print()

def operaciones_basicas():
    """Demuestra operaciones aritméticas y lógicas básicas"""
    print("=== OPERACIONES BÁSICAS ===")
    
    a = 10
    b = 3
    
    print(f"a = {a}, b = {b}")
    print(f"Suma: a + b = {a + b}")
    print(f"Resta: a - b = {a - b}")
    print(f"Multiplicación: a * b = {a * b}")
    print(f"División: a / b = {a / b}")
    print(f"División entera: a // b = {a // b}")
    print(f"Módulo: a % b = {a % b}")
    print(f"Potencia: a ** b = {a ** b}")
    
    print()

def estructuras_control():
    """Demuestra estructuras de control: if/else y bucles"""
    print("=== ESTRUCTURAS DE CONTROL ===")
    
    # Condicionales
    edad = 20
    print(f"Edad: {edad}")
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    
    # Bucle for
    print("\nConteo del 1 al 5:")
    for i in range(1, 6):
        print(f"Número: {i}")
    
    # Bucle while
    print("\nConteo regresivo desde 3:")
    contador = 3
    while contador > 0:
        print(f"Contador: {contador}")
        contador -= 1
    print("¡Despegue!")
    
    print()

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo
    
    Args:
        base (float): Base del rectángulo
        altura (float): Altura del rectángulo
    
    Returns:
        float: Área del rectángulo
    """
    return base * altura

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo
    
    Args:
        radio (float): Radio del círculo
    
    Returns:
        float: Área del círculo
    """
    import math
    return math.pi * radio ** 2

def demostracion_funciones():
    """Demuestra el uso de funciones"""
    print("=== FUNCIONES ===")
    
    # Área de rectángulo
    base = 5
    altura = 3
    area_rect = calcular_area_rectangulo(base, altura)
    print(f"Área del rectángulo (base={base}, altura={altura}): {area_rect}")
    
    # Área de círculo
    radio = 4
    area_circ = calcular_area_circulo(radio)
    print(f"Área del círculo (radio={radio}): {area_circ:.2f}")
    
    print()

def interaccion_usuario():
    """Demuestra la interacción con el usuario"""
    print("=== INTERACCIÓN CON USUARIO ===")
    
    try:
        nombre = input("¿Cuál es tu nombre? ")
        print(f"¡Hola, {nombre}!")
        
        edad_str = input("¿Cuántos años tienes? ")
        edad = int(edad_str)
        
        if edad >= 18:
            print(f"{nombre}, eres mayor de edad ({edad} años)")
        else:
            años_faltantes = 18 - edad
            print(f"{nombre}, te faltan {años_faltantes} años para ser mayor de edad")
            
    except ValueError:
        print("Error: Por favor ingresa un número válido para la edad")
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario")
    
    print()

def main():
    """Función principal que ejecuta todas las demostraciones"""
    print("=" * 50)
    print("    P01 - PYTHON FUNDAMENTALS FOR ISC")
    print("    Fundamentos de Python para ISC")
    print("=" * 50)
    print()
    
    # Ejecutar todas las demostraciones
    mostrar_tipos_datos()
    operaciones_basicas()
    estructuras_control()
    demostracion_funciones()
    
    # Preguntar si quiere interactuar
    print("¿Deseas probar la sección interactiva? (s/n): ", end="")
    respuesta = input().lower()
    if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
        interaccion_usuario()
    
    print("¡Gracias por usar el programa de demostración!")
    print("Fin del programa P01 - Python Fundamentals for ISC")

if __name__ == "__main__":
    main()