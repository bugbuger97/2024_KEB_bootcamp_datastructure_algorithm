import mymath
if __name__ == "__main__":
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f"{n}C{r} = {mymath.nCr(n,r)}\n")

    # 시간 복잡도(Time complexity) : operation이 일어난 횟수 측정
    # big-O natation == worst time case