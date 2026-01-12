"""
En esta kata, se solicita al usuario un numero, si este es:

- Divisible entre 3, el programa debe imprimir "Fizz"

- Divisible entre 5, el programa debe imprimit "Buzz"

- Divisible entre 3 y entre 5, el programa debe imprimir "FizzBuzz"

- Si no es divisible ni entre 3 ni entre 5, debe imprimir el número
"""
# iteracion 1:
#   1- crear un repositiorio Fizzbuzz excepciones enviar por chat la url
#   2- primera implementacion del problema
if __name__=="__main__":
    
    numero =int(input("introduzca un numero: "))
    
    if(numero%3==0 and numero%5==0):
        print("fizzBuzz")
    elif numero%3==0:
        print("fizz")
    elif(numero%5==0):
        print("Buzz")
    else:
        print(numero)