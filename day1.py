def factorial(number) -> int:
    """
    factorial function by recursion
    :param number: number
    :return: number!
    """
    if number <= 1:
        return 1
    else:
        return number * factorial(number-1)

def nCr(n,r) -> int:
    '''
    combination function
    :param n: n
    :param r: r
    :return: nCr
    '''
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerator / denominator)

if __name__ == "__main__":
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f"{n}C{r} = {nCr(n,r)}\n")