class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Caso extremo vital: si nos dan un string vacío, regresamos lista vacía
        if not digits:
            return []
        
        # 1. Nuestro mapa del teclado numérico
        teclado = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        resultado = []
        
        # 2. Función recursiva para el Backtracking
        def backtrack(indice, combinacion_actual):
            # Condición de paro: si la combinación tiene el mismo tamaño que los dígitos
            if len(combinacion_actual) == len(digits):
                resultado.append(combinacion_actual)
                return
            
            # Obtenemos las letras que corresponden al dígito actual
            letras_posibles = teclado[digits[indice]]
            
            # Exploramos cada letra
            for letra in letras_posibles:
                # Llamada recursiva: avanzamos al siguiente índice y agregamos la letra
                backtrack(indice + 1, combinacion_actual + letra)
                
        # 3. Disparamos la recursión empezando en el índice 0 y con string vacío
        backtrack(0, "")
        
        return resultado
