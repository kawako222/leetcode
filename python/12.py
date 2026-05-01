def intToRoman(num: int) -> str:
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1) , ("I")
    ]
    
    resultado = []
    
    for valor, simbolo in valores:
        if num == 0:
            break
        
        cantidad, num = divmod(num, valor)
        
        resultado.append(simbolo * cantidad)
    
    return "".join(resultado)

print(intToRoman(3749))
