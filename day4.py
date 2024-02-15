import random
# 선택 정렬 : 가장 작은 값을 뽑는 작동을 반복 후 정렬함. -> O(n^2)
def selection_sort(arr):
    arr_size = len(arr)
    for i in range(0,arr_size-1):
        Min_index = i
        for j in range(i+1,arr_size):
            if arr[Min_index] > arr[j]:
                Min_index = j
        arr[i], arr[Min_index] = arr[Min_index], arr[i]
    return arr
# 삽입 정렬 : 오름차순일때의 자신의 위치를 찾아 데이터를 삽입하는 정렬 -> O(n^2)
def insertion_sort(arr):
    arr_size = len(arr)
    for i in range(0,arr_size):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr
# 버블 정렬 : 바로 전과 후의 데이터를 비교해서 오름차순을 하는 정렬 -> O(n^2)
def bubble_sort(arr):
    arr_size = len(arr)
    for i in range(arr_size-1,0,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# 퀵 정렬 : pivot을 하나 정해서 그룹을 2개로 나누어 정렬하는 방법(재귀를 사용함.) -> O(n^2)
def quick_sort(arr):
    arr_size = len(arr)
    if arr_size <= 1:
        return arr
    pivot = arr[arr_size//2]
    left_arr, equal_arr, right_arr = [], [], []
    for i in arr:
        if i < pivot:
            left_arr.append(i)
        elif i > pivot:
            right_arr.append(i)
        else:
            equal_arr.append(i)
    return quick_sort(left_arr) + equal_arr + quick_sort(right_arr)

arr = [random.randint(1,10) for _ in range(10)]
if __name__ == "__main__":
    print(selection_sort(arr))
    print(insertion_sort(arr))
    print(bubble_sort(arr))
    print(quick_sort(arr))