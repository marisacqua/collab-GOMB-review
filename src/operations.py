'''
Arithmetic operations
'''
import pytest

def summation(a, b):
    return a + b

def sub(a, b):
    #TODO: would be good to give this function a better name
    return a - b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero is not allowed.")

def test_answer():
    assert division(10, 2) == 6

def multiplication(a, b):
    return a * b 
