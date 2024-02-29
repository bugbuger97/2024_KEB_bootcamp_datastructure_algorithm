'''
recursion
자기 자신을 호출하는 것

함수 호출 -> 1.Function() -> 함수 호출 -> 2.Function() -> 내용물 반환 -> return(2.Function() 끝) -> 1.Function() -> 함수 close
'''

def Function():
    global cnt
    print("함수 호출")
    cnt -= 1
    if cnt == 0:
        print('내용물 반환')
        return
    Function()
    print('함수 close')

cnt = 2
if __name__ == "__main__":
    Function()