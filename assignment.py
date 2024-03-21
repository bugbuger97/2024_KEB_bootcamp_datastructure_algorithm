# 연습 문제1: 원소 삭제, 삽입
import array
class Array_List:
    def __init__(self,n):
        self.capacity = n
        self.array = array.array('h',[0]*self.capacity)
        self.size = 0
    def full(self) -> bool:
        '''
        배열이 꽉 차면 True return, 아니면 False return
        :return: bool flag
        '''
        if self.size == self.capacity:
            return True
        else:
            return False
    def add(self,idx,item) -> array:
        '''
        주어진 index에 데이터 삽입. 데이터 삽입.
        해당 index에 데이터가 존재할 경우, 다음 element들을 오른쪽으로 한칸씩 이동 후 해당 위치에 삽입
        :param idx: index
        :param item: value
        :return: array
        '''
        if self.full():
            return f'배열이 모두 찼기 때문에 더 이상 삽입이 불가능합니다.'
        if self.array[idx] == 0:
            self.array[idx] = item
        else:
            for i in range(self.size-1,idx-1,-1): # i = self.size-1 ~ idx
                self.array[i+1] = self.array[i]
            self.array[idx] = item
        self.size += 1
        return self.array
    def print(self):
        for i in range(self.size):
            print(self.array[i],end=' ')
        print()
    def sset(self,idx,item) -> array:
        self.array[idx] = item
        return self.array
    def remove(self,idx) -> array:
        if idx == self.size-1:
            self.array[idx] = 0
            return self.array
        for i in range(idx,self.size):
            self.array[i] = self.array[i+1]
        self.size -= 1
        return self.array
    def find(self,item) -> int:
        idx = 0
        for i in self.array:
            if i == item:
                return idx
            idx+=1
        return -1

if __name__ == '__main__':
    arr_list = Array_List(6)
    arr_list.add(0,5)
    arr_list.add(0, 2)
    arr_list.add(0, 8)
    arr_list.add(1, 4)
    arr_list.print()
    arr_list.remove(2)
    arr_list.remove(0)
    arr_list.print()
    arr_list.add(0, 3)
    arr_list.add(1, 1)
    arr_list.print()
    print(f'4의 index는 {arr_list.find(4)}')