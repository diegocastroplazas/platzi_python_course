def obtenerPrimeraLetraNoRepetida(secuencia):
    result = None
    for s in secuencia:
        if (secuencia.count(s) < 2):
            result = s
            break
    return result

def main():
    secuencia = str(input("Ingresa una secuencia de caracteres: "))
    result = obtenerPrimeraLetraNoRepetida(secuencia)
    if ( result == None):
        print ("Todas las letras se repiten")
    else:
        print ("La primera letra que no se repite es: " + result )

if __name__ == '__main__':
    main()