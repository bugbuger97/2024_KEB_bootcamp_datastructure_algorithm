# self study 10-1

def recursion_plus(a,b):
    if a > b:
        a,b = b,a
        return recursion_plus(a,b)
    elif a == b:
        return b
    else:
        return recursion_plus(a+1,b) + a

if __name__ == "__main__":
    num1 = int(input('숫자1 --> '))
    num2 = int(input('숫자2 --> '))
    print(recursion_plus(num1,num2))