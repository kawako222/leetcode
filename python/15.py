class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 1. Ordenamos el arreglo de menor a mayor
        nums.sort()
        resultado = []
        
        # 2. Recorremos el arreglo fijando el primer número
        for i in range(len(nums)):
            # Truco para evitar tríos duplicados: 
            # Si el número actual es igual al anterior, lo saltamos
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 3. Inicializamos nuestros dos punteros
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                suma = nums[i] + nums[left] + nums[right]
                
                # Si la suma es mayor a 0, necesitamos un número más pequeño
                if suma > 0:
                    right -= 1
                # Si la suma es menor a 0, necesitamos un número más grande
                elif suma < 0:
                    left += 1
                # ¡Encontramos un trío que suma 0!
                else:
                    resultado.append([nums[i], nums[left], nums[right]])
                    
                    # Movemos ambos punteros para seguir buscando
                    left += 1
                    right -= 1
                    
                    # Otro truco para evitar duplicados:
                    # Si el nuevo 'left' es igual al anterior, lo seguimos moviendo
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return resultado
