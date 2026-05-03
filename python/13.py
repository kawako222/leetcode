class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Creamos nuestro Hash Map (Diccionario) con los valores
        valores = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # 2. Recorremos el string letra por letra
        for i in range(n):
            # Si no estamos en la última letra Y el valor actual es MENOR que el siguiente
            if i < n - 1 and valores[s[i]] < valores[s[i + 1]]:
                # Aplicamos la regla de la resta
                total -= valores[s[i]]
            else:
                # Si no, simplemente sumamos
                total += valores[s[i]]
                
        return total
