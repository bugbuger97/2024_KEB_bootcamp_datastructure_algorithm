# 3-2
def print_Poly(fx):
    term = len(fx)
    poly_str = "f(x) = "
    for i in range(len(fx)):
        coef = fx[i]
        term -= 1
        if coef == 0:
            continue
        if coef > 0:
            poly_str += "+"
        poly_str += str(coef) + "x^" + str(term) + " "
    return poly_str
def calcPoly(x_Value, fx):
    result_Value = 0
    term = len(fx) - 1
    for i in range(len(fx)):
        coef = fx[i]
        result_Value += coef * x_Value ** term
        term -= 1
    return result_Value

fx = [7, -4, 0, 5]
if __name__ == "__main__":
    pStr = print_Poly(fx)
    print(pStr)
    xValue = int(input("x 값 = "))
    pxValue = calcPoly(xValue, fx)
    print(pxValue)