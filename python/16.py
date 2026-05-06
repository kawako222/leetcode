class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # 1. Ordenamos el arreglo
        nums.sort()
        
        # Inicializamos nuestra "mejor suma" con infinito
        # para que cualquier primera suma que encontremos la reemplace de inmediato
        suma_mas_cercana = float('inf')
        
        # 2. Recorremos el arreglo
        for i in range(len(nums) - 2):
            # 3. Inicializamos los dos punteros
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                suma_actual = nums[i] + nums[left] + nums[right]
                
                # Calculamos la "distancia" al target. 
                # Si esta suma está más cerca que la anterior, la guardamos.
                if abs(suma_actual - target) < abs(suma_mas_cercana - target):
                    suma_mas_cercana = suma_actual
                
                # Optimizador estrella: si le dimos exactamente al blanco, 
                # es imposible acercarnos más. Terminamos el programa aquí.
                if suma_actual == target:
                    return suma_actual
                
                # Si la suma actual es menor al target, 
                # movemos el puntero izquierdo para sumar un número más grande
                elif suma_actual < target:
                    left += 1
                # Si la suma actual es mayor al target, 
                # movemos el puntero derecho para sumar un número más pequeño
                else:
                    right -= 1
                    
        return suma_mas_cercana
