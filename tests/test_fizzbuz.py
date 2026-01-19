from main import fizzbuzz
import pytest
"""En esta kata, se solicita al usuario un numero entre 1 y 100, si este es:

- Divisible entre 3, el programa debe imprimir "Fizz"

- Divisible entre 5, el programa debe imprimit "Buzz"

- Divisible entre 3 y entre 5, el programa debe imprimir "FizzBuzz"

- Si no es divisible ni entre 3 ni entre 5, debe imprimir el número
"""
#Validacion tipos de entrada
def test_fizzbuzString():
    #valida que el programa de error ante una entrada de texto
    with pytest.assertRaises(ValueError):

        fizzbuzz("2")
def test_fizzbuzDouble():
    #valida que el programa de error ante una entrada Double
    with pytest.assertRaises(ValueError):

        fizzbuzz(2.52)
def test_fizzbuzNegativos():
    #valida que el programa de error ante una entrada entera pero negativo
    with pytest.assertRaises(ValueError):

        fizzbuzz(-5)

#Validacion limites
def test_fizzbuzMenorde1():
    #valida que el programa de error ante un numero menor de 1
    with pytest.assertRaises(ValueError):

        fizzbuzz(-5)
def test_fizzbuz1():
    #valida que el programa no de error ante ante la entrada numerica 1
    assert fizzbuzz(1) =="1"

def test_fizzbuzMayorde100():
    #valida que el programa de error ante un numero mayor de 100
    with pytest.assertRaises(ValueError):

        fizzbuzz(150)
def test_fizzbuz100():
    #valida que el programa no de error ante ante la entrada numerica 100
    assert fizzbuzz(100) =="Buzz"

#Validacion reglas de juego
def test_fizzbuz3():
    #valida que el programa devuelve fizz ante la entrada numerica 3
    assert fizzbuzz(3) =="Fizz"
    
def test_fizzbuz5():
    #valida que el programa devuelve buzz ante la entrada numerica 5
    assert fizzbuzz(5) =="Buzz"
def test_fizzbuz15():
    #valida que el programa devuelve fizzbuzz ante la entrada numerica 15
    assert fizzbuzz(15) =="FizzBuzz"
def test_fizzbuz2():
    #valida que el programa devuelve 2 ante la entrada numerica 2
    pass
