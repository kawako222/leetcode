def generateParenthesis(n):
    resultado = []
    
    def backtrack(cadena_actual, abiertos, cerrados):
        # Caso Base: Si la cadena tiene la longitud máxima, encontramos una combinación válida
        if len(cadena_actual) == 2 * n:
            resultado.append(cadena_actual)
            return
        
        # Regla 1: Si aún nos quedan paréntesis abiertos por usar, ponemos uno
        if abiertos < n:
            backtrack(cadena_actual + "(", abiertos + 1, cerrados)
            
        # Regla 2: Solo podemos cerrar si hay un abierto esperando su pareja
        if cerrados < abiertos:
            backtrack(cadena_actual + ")", abiertos, cerrados + 1)
            
    # Iniciamos la recursividad con una cadena vacía y los contadores en 0
    backtrack("", 0, 0)
    return resultado
