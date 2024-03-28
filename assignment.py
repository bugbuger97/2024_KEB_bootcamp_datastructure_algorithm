import array
'''
Q1. 주어진 add함수를 수정하여 배열 중간에 원소가 삽입 되도록 해라.
만약 array가 다 찼다면, return full
아니라면, arr[idx]에 값이 있다면, 값이 없다면으로 나누자.
arr[idx]에 값이 있다면 -> idx부터 size까지 한칸씩 이동 -> 목표 idx에 값 삽입 
arr[idx]값이 없다면 -> 그냥 바로 삽입 
'''
class ArrayList:
    def __init__(self,n):
        self.capacity = n
        self.array = array.array('h',[0]*self.capacity)
        self.size=0
    def is_full(self) -> bool:
        if self.size == self.capacity:
            return True
        else:
            return False
    def add(self,idx,item): # Q1
        if self.is_full():
            print('array가 다 찼기 때문에, 더 이상 삽입할 수 없습니다.')
        else:
            if self.array[idx] == 0:
                self.array[idx] = item
            else:
                for _ in range(self.size-1,idx-1,-1):
                    self.array[_+1] = self.array[_]
                self.array[idx] = item
        self.size += 1
        return self.array
    def print(self):
        for i in range(self.size):
            print(self.array[i],end=' ')
        print()
    def is_empty(self)->bool:
        if self.size == 0:
            return True
        else:
            return False
    def remove(self,idx):
        if self.is_empty():
            print('다 비어서 제거할 값이 없어요')
            return
        else:
            if self.array[idx] == 0:
                print('이 인덱스에 제거할 값이 없어요')
                return
            else:
                self.array[idx] = 0
                for _ in range(idx,self.size-1):
                    self.array[_] = self.array[_+1]
                self.size -= 1
            return self.array
    def sset(self,idx,item):
        self.array[idx] = item
        return self.array
    def find(self, item):
        for _ in range(self.size):
            if self.array[_] == item:
                return _
        return -1

# from arraylist import *
if __name__ == '__main__':
    arr_list = ArrayList(6)
    arr_list.add(0,5)
    arr_list.add(1,2)
    arr_list.add(2,8)
    arr_list.add(3,4)
    arr_list.add(0,1)
    arr_list.add(0,2)
    arr_list.print()

    if arr_list.is_full():
        print('배불러요')
    arr_list.remove(0)
    print(arr_list.find(0))
    arr_list.print()