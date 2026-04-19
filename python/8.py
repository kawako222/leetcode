class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Eliminar espacios en blanco al inicio
        s = s.lstrip()
        
        # Si el string está vacío después de limpiar, retornamos 0
        if not s:
            return 0
            
        sign = 1
        index = 0
        
        # 2. Determinar el signo
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
            
        res = 0
        
        # 3. Leer los dígitos numéricos
        while index < len(s) and s[index].isdigit():
            # Convertimos el carácter a número y lo acumulamos
            digit = int(s[index])
            res = (res * 10) + digit
            index += 1
            
        # Aplicamos el signo al resultado final
        res *= sign
        
        # 4. Redondeo (Clamping) a los límites de 32 bits
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        
        if res < MIN_INT:
            return MIN_INT
        if res > MAX_INT:
            return MAX_INT
            
        return res
