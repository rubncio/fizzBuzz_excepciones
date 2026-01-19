"""
En esta kata, se solicita al usuario un numero, si este es:

- Divisible entre 3, el programa debe imprimir "Fizz"

- Divisible entre 5, el programa debe imprimit "Buzz"

- Divisible entre 3 y entre 5, el programa debe imprimir "FizzBuzz"

- Si no es divisible ni entre 3 ni entre 5, debe imprimir el número
"""
"""que sea una funcino mas simple en el que reciba un numero n y devuelva un string"""
def fizzbuzz(numero) -> str:
    if numero<1 or numero>100 or not isinstance(numero, int):
                raise ValueError
    if(numero%3==0 and numero%5==0):
        return "FizzBuzz"
    elif numero%3==0:
        return "Fizz"
    elif(numero%5==0):
        return "Buzz"
    else:
        return str(numero)

if __name__=="__main__":
    """while(True):
        try:
            numero =int(input("introduzca un numero del 1 al 100: "))
            if(numero<1 or numero>100):
                raise ValueError
            fizzbuzz(numero)

        except(ValueError):
            print("Valor incorrecto para la cifra")"""
    print(fizzbuzz(3))
        
    
    
    