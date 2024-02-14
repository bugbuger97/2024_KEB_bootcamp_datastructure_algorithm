def decimal_to_octal(number: int) -> str:
    """
    decimal number to octal number (by recursion)
    :param number: integer (base dec)
    :return: string(base octal)
    """
    if number < 8:
        return str(number)
    else:
        return decimal_to_octal(n//8) + str(n%8)

if __name__ == "__main__":
    n = int(input("Input decimal number : "))
    print(decimal_to_octal(n))