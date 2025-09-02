#!/usr/bin/env python3
"""
Tests para P01 - Python Fundamentals
Pruebas básicas para validar las funciones del programa principal
"""

import math
import sys
import os

# Agregar el directorio actual al path para importar main
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import calcular_area_rectangulo, calcular_area_circulo

def test_area_rectangulo():
    """Prueba la función de cálculo de área de rectángulo"""
    print("Probando calcular_area_rectangulo...")
    
    # Caso 1: Rectángulo simple
    area = calcular_area_rectangulo(5, 3)
    expected = 15
    assert area == expected, f"Esperado {expected}, obtenido {area}"
    print(f"  ✓ Área rectángulo (5x3) = {area}")
    
    # Caso 2: Rectángulo con decimales
    area = calcular_area_rectangulo(2.5, 4.0)
    expected = 10.0
    assert area == expected, f"Esperado {expected}, obtenido {area}"
    print(f"  ✓ Área rectángulo (2.5x4.0) = {area}")
    
    # Caso 3: Rectángulo unitario
    area = calcular_area_rectangulo(1, 1)
    expected = 1
    assert area == expected, f"Esperado {expected}, obtenido {area}"
    print(f"  ✓ Área rectángulo (1x1) = {area}")

def test_area_circulo():
    """Prueba la función de cálculo de área de círculo"""
    print("Probando calcular_area_circulo...")
    
    # Caso 1: Radio entero
    area = calcular_area_circulo(1)
    expected = math.pi
    assert abs(area - expected) < 0.0001, f"Esperado {expected}, obtenido {area}"
    print(f"  ✓ Área círculo (radio=1) = {area:.4f}")
    
    # Caso 2: Radio decimal
    area = calcular_area_circulo(2.0)
    expected = math.pi * 4
    assert abs(area - expected) < 0.0001, f"Esperado {expected}, obtenido {area}"
    print(f"  ✓ Área círculo (radio=2.0) = {area:.4f}")
    
    # Caso 3: Radio cero
    area = calcular_area_circulo(0)
    expected = 0
    assert area == expected, f"Esperado {expected}, obtenido {area}"
    print(f"  ✓ Área círculo (radio=0) = {area}")

def test_tipos_basicos():
    """Prueba los tipos de datos básicos usados en el programa"""
    print("Probando tipos de datos básicos...")
    
    # Entero
    numero_entero = 42
    assert isinstance(numero_entero, int), f"Se esperaba int, obtenido {type(numero_entero)}"
    print(f"  ✓ Número entero: {numero_entero} es de tipo {type(numero_entero).__name__}")
    
    # Float
    numero_decimal = 3.14159
    assert isinstance(numero_decimal, float), f"Se esperaba float, obtenido {type(numero_decimal)}"
    print(f"  ✓ Número decimal: {numero_decimal} es de tipo {type(numero_decimal).__name__}")
    
    # String
    texto = "Hola, ISC!"
    assert isinstance(texto, str), f"Se esperaba str, obtenido {type(texto)}"
    print(f"  ✓ Texto: '{texto}' es de tipo {type(texto).__name__}")
    
    # Boolean
    verdadero = True
    assert isinstance(verdadero, bool), f"Se esperaba bool, obtenido {type(verdadero)}"
    print(f"  ✓ Booleano: {verdadero} es de tipo {type(verdadero).__name__}")
    
    # List
    lista_numeros = [1, 2, 3, 4, 5]
    assert isinstance(lista_numeros, list), f"Se esperaba list, obtenido {type(lista_numeros)}"
    print(f"  ✓ Lista: {lista_numeros} es de tipo {type(lista_numeros).__name__}")

def test_operaciones_aritmeticas():
    """Prueba operaciones aritméticas básicas"""
    print("Probando operaciones aritméticas...")
    
    a, b = 10, 3
    
    # Suma
    resultado = a + b
    assert resultado == 13, f"Suma incorrecta: {a} + {b} = {resultado}"
    print(f"  ✓ Suma: {a} + {b} = {resultado}")
    
    # Resta  
    resultado = a - b
    assert resultado == 7, f"Resta incorrecta: {a} - {b} = {resultado}"
    print(f"  ✓ Resta: {a} - {b} = {resultado}")
    
    # Multiplicación
    resultado = a * b
    assert resultado == 30, f"Multiplicación incorrecta: {a} * {b} = {resultado}"
    print(f"  ✓ Multiplicación: {a} * {b} = {resultado}")
    
    # División
    resultado = a / b
    expected = 10/3
    assert abs(resultado - expected) < 0.0001, f"División incorrecta: {a} / {b} = {resultado}"
    print(f"  ✓ División: {a} / {b} = {resultado:.4f}")

def main():
    """Ejecuta todas las pruebas"""
    print("=" * 50)
    print("    TESTS - P01 PYTHON FUNDAMENTALS")
    print("=" * 50)
    print()
    
    try:
        test_tipos_basicos()
        print()
        
        test_operaciones_aritmeticas()
        print()
        
        test_area_rectangulo()
        print()
        
        test_area_circulo()
        print()
        
        print("🎉 ¡Todas las pruebas pasaron exitosamente!")
        
    except AssertionError as e:
        print(f"❌ Error en prueba: {e}")
        return 1
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)