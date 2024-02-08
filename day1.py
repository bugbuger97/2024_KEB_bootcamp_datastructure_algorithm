def factorial(number) -> int:
    if number <= 0:
        return 1
    else:
        return number * factorial(number-1)

def nCr(n,r) -> float:
    '''
    조합 함수
    :param n: n
    :param r: r
    :return: nCr
    '''
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return numerator / denominator

if __name__ == "__main__":
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f"{n}C{r} = {nCr(n,r)}\n")