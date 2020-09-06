def e_cuadratica(n):
    """
    """
    resultado = 0
    

    for i in range(n+1):
        denominador = 1
        j = i
        while j != 0:
            
            denominador = denominador*j
            j -= 1
        resultado = resultado+(1/denominador)
    
    return 0


def e_lineal(n):
    n = 0
    return 0
