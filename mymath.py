import time
def time_taken(func) -> float:
    '''
    print time taken
    :param func: fuction
    :return: time taken
    '''
    def wrapper(*args,**kwargs) -> None:
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"time elaped : {end-start}")
        return result
    return wrapper
def factorial(number) -> int:
    """
    factorial function by recursion
    use stack memory
    :param number: number
    :return: number!
    """
    if number <= 1:
        return 1
    else:
        return number * factorial(number-1)
@time_taken
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