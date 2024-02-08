import random
if __name__ == "__main__":
    result = random.randint(1,100)
    cnt = 0
    opportunities = 7
    while cnt < opportunities:
        cnt += 1
        response = int(input("Input number : "))
        if result > response:
            print("up")
        elif result < response:
            print("down")
        else:
            print("correct!!")
            print(f"{cnt}번만에 정답 번호 : {result}인 것을 맞추었습니다.")
            break
    else:
        print("failed!! You lose......")