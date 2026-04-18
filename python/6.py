class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Caso base: Si solo hay una fila o el string es más corto que las filas,
        # no hay zigzag posible, se devuelve tal cual.
        if numRows == 1 or numRows >= len(s):
            return s

        # Creamos una lista de strings para representar cada fila.
        rows = ["" for _ in range(numRows)]
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            
            # Si estamos en la primera o última fila, cambiamos la dirección (el "rebote").
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Movemos el puntero de la fila según la dirección actual.
            current_row += 1 if going_down else -1

        # Al final, unimos todas las filas en un solo string.
        return "".join(rows)
