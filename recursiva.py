def factorial(numero):
    if (numero == 0):
        return 1
    fact = numero * factorial(numero - 1)
    return fact
if __name__== "__main__":
    n = int(eval(input("Ingresar numero")))
    result = factorial(n)
    print (result)