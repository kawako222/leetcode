class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Inicializamos punteros en los extremos
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # El ancho es la distancia entre punteros
            width = right - left
            
            # La altura del agua es la de la pared más corta
            current_height = min(height[left], height[right])
            
            # Calculamos el área y actualizamos el máximo
            current_area = width * current_height
            max_water = max(max_water, current_area)
            
            # Movilizamos el puntero de la pared más baja
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
