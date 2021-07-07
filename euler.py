def e_cuadratica(n):
    """
    Entradas: Cantidad de veces que se itera
    Salidas: Resultado de la aproximación a e en complejidad temporal cuadrática
    """

    resultado = 0

    for i in range(n):
        denominador = 1
        j = i
        while j != 0:
            
            denominador = denominador*j
            j -= 1
        resultado = resultado+(1/denominador)

    return resultado


def e_lineal(n):
    """
    Entradas: Cantidad de veces que se itera
    Salidas: Resultado de la aproximación a e en complejidad temporal lineal
    """

    denominador = 1
    resultado = 0

    for i in range(1,n+1):
        resultado += 1/denominador
        denominador = denominador*i

    return resultado
