class Solution:
    def reverse(self, x: int) -> int:
        # 1. Definir los límites de un entero de 32 bits con signo
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        
        # 2. Inicializar el resultado
        res = 0
        
        # 3. Extraer el signo y trabajar con el valor absoluto para simplificar el módulo
        # (En Python el módulo de números negativos funciona diferente que en C/Java)
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # 4. Proceso de inversión matemática
        while x != 0:
            # Obtener el último dígito
            digit = x % 10
            # Eliminar el último dígito de x
            x //= 10
            
            # 5. Comprobar el overflow ANTES de multiplicar (crítico para la restricción de 32 bits)
            # Si res ya es mayor que MAX_INT // 10, al multiplicarlo por 10 se desbordará.
            if res > MAX_INT // 10 or (res == MAX_INT // 10 and digit > 7):
                return 0
                
            # Como trabajamos con el valor absoluto, no necesitamos checar el MIN_INT aquí,
            # pero la lógica general para positivos nos protege.
            
            # Añadir el dígito al resultado invertido
            res = (res * 10) + digit
            
        # 6. Devolver el resultado con su signo original
        return res * sign
