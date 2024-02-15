# 응용 01

def add_List():
    global Linear_List
    name = input("추가할 data : ")
    number = int(input("data의 number : "))
    Linear_List = [(name,number)] + Linear_List
    return Linear_List

Linear_List = [('가',200),('나',180),('다',160),('라',140),('마',120)]
if __name__ == "__main__":
    while True:
        print(add_List())
        if Linear_List[0][1] == 0:
            break