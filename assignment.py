# 응용 02
def print_Poly(fx):
    poly_str = "f(x) = "
    for i in range(len(fx)):
        coef = fx[i]
        if coef == 0:
            continue
        if coef > 0:
            poly_str += "+"
        poly_str += str(coef) + "x^" + str(term[i]) + " "
    return poly_str
def calc_Poly(x_Value, fx):
    result_Value = 0
    for i in range(len(fx)):
        coef = fx[i]
        result_Value += coef * x_Value ** term[i]
    return result_Value

term = [300,20,0,0]
fx = [7, -4, 0, 5]
if __name__ == "__main__":
    Str = print_Poly(fx)
    print(Str)
    x_Value = int(input("x 값 = "))
    fx_Value = calc_Poly(x_Value, fx)
    print(fx_Value)