'''
Circular Queue
FIFO의 원칙을 유지하면서 큐의 입구와 출구를 연결한 구조이다.
'''
def is_Queue_full():
	global size, queue, front, rear
	if (rear + 1) % size == front:
		return True
	else:
		return False
def is_Queue_empty():
	global size, queue, front, rear
	if front == rear:
		return True
	else:
		return False
def enQueue(data):
	global size, queue, front, rear
	if is_Queue_full():
		print("Queue is full")
		return
	rear = (rear + 1) % size
	queue[rear] = data
def deQueue():
	global size, queue, front, rear
	if is_Queue_empty():
		print("Queue is empty")
		return None
	front = (front+1) % size
	data = queue[front]
	queue[front] = None
	return data
def peek():
	global size, queue, front, rear
	if is_Queue_empty():
		print("Queue is empty")
		return None
	return queue[(front+1)%size]

size = 6
queue = [None for _ in range(size)]
front = rear = 0
if __name__ == "__main__":
	Sum = 0
	temp = [("사용",9),("고장",3),("환불",4),("환불",4),("고장",3)]
	print(f'귀하의 대기 예상시간은 0 분입니다.')
	print(f'현재 대기 콜 --> {queue}\n')
	for data in temp:
		enQueue(data)
		if is_Queue_full():
			print(f'최종 대기 콜 --> {queue}')
			print('프로그램 종료\n')
			break
		Sum += queue[rear][1]
		print(f'귀하의 대기 예상시간은 {Sum} 분입니다.')
		print(f'현재 대기 콜 --> {queue}\n')