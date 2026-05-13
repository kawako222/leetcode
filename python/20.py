def isValid(s: str) -> bool:
    # Diccionario para mapear los cierres con sus aperturas
    mapping = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        # Si es un paréntesis de cierre
        if char in mapping:
            # Sacamos el elemento del tope si el stack no está vacío
            top_element = stack.pop() if stack else '#'
            
            # Si el tipo de apertura no coincide con el cierre esperado
            if mapping[char] != top_element:
                return False
        else:
            # Si es de apertura, lo agregamos al stack
            stack.append(char)

    # Si el stack está vacío, es válido
    return not stack
