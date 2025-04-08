def decimal_a_romano(numero):
   
    valores_romanos = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    resultado = ""
    
    for valor, simbolo in valores_romanos:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    
    return resultado

numero_decimal = int(input("Ingresa un número decimal: "))
numero_romano = decimal_a_romano(numero_decimal)
print(f"El número romano es: {numero_romano}")
