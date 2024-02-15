'''
Linear List
데이터를 입략 순서대로 저장하는 데이터 구조
'''

# Linear_List = [0,1,2,3]
#
# for i in range(len(Linear_List)):
#     print(id(Linear_List[i]))

# 3-1
def delete(pos):
    global Linear_List
    if pos < 0 or pos > len(Linear_List):
        print("데이터를 삭제할 범위를 벗어남")
        return
    Len = len(Linear_List)
    del(Linear_List[pos:])
    return

Linear_List = ['가', '나', '다', '라', '마','바','사']

if __name__ == "__main__":
    print(Linear_List)
    delete(1)
    print(Linear_List)
    delete(3)
    print(Linear_List)