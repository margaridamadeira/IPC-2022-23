# -*- coding: utf-8 -*-

"""
Conversão de temperaturas - extrato
(c) Margarida Madeira e Moura, 2022
"""

def f2c(fahrenheit):
    """Converte uma temperatura de fahrenheit para celsius."""

    resultado = (fahrenheit - 32) / 1.8
    return resultado


def c2k(celsius):
    """Converte uma temperatura de celsius para kelvin."""

    resultado = celsius + 273.15
    return resultado


def f2k(fahrenheit):
    """Converte uma temperatura de fahrenheit para kelvin."""
    return c2k(f2c(fahrenheit))

def test_f2k():
    """Entrada e saída de dados"""
    x = float(input())
    z = f2k(x)
    print(z)
    
if __name__ == '__main__':
    test_f2k()



