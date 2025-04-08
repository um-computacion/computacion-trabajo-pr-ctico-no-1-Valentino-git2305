def roman_to_decimal(roman):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

print (roman_number = "MMIV")   
decimal_number = roman_to_decimal(roman_number)
print(f"El número decimal de {roman_number} es {decimal_number}")