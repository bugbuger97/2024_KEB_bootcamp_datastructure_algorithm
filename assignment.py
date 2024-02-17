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

size = 5
queue = [None for _ in range(size)]
front = rear = 0
if __name__ == "__main__":
	print(queue)
	print(f"front = {front}, rear = {rear}")
	enQueue("a")
	print(f"front = {front}, rear = {rear}")
	print(queue)
	enQueue("b")
	print(f"front = {front}, rear = {rear}")
	print(queue)
	enQueue("c")
	print(f"front = {front}, rear = {rear}")
	print(queue)
	enQueue("d")
	print(f"front = {front}, rear = {rear}")
	print(queue)
	enQueue("e")
	print(f"front = {front}, rear = {rear}")
	print(queue)
	deQueue()
	print(queue)
	print(f"front = {front}, rear = {rear}")
	deQueue()
	print(queue)
	print(f"front = {front}, rear = {rear}")
	deQueue()
	print(queue)
	print(f"front = {front}, rear = {rear}")
	enQueue("x")
	print(queue)
	print(f"front = {front}, rear = {rear}")