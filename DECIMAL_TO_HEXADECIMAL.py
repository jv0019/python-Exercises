def decimal_to_hexadecimal(decimal_number):
    if decimal_number < 0:
        return '-' + decimal_to_hexadecimal(-decimal_number)
    elif decimal_number == 0:
        return '0'
    else:
        hex_digits = "0123456789ABCDEF"
        hexadecimal = ""
        while decimal_number > 0:
            remainder = decimal_number % 16
            hexadecimal = hex_digits[remainder] + hexadecimal
            decimal_number = decimal_number // 16
        return hexadecimal

# Example usage
decimal_number = int(input("Enter a decimal number: "))
print(f"Hexadecimal equivalent: {decimal_to_hexadecimal(decimal_number)}")