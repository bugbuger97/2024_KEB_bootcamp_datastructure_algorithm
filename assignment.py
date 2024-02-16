# Queue 응용 1
def is_Queue_full():
	global SIZE, queue, front, rear
	if rear == SIZE-1:
		return True
	else:
		return False
def is_Queue_empty():
	global SIZE, queue, front, rear
	if front == rear:
		return True
	else:
		return False
def enQueue(data):
	global SIZE, queue, front, rear
	if is_Queue_full():
		print("Queue is full")
		return
	rear+=1
	queue[rear] = data
def deQueue():
	global SIZE, queue, front, rear
	if is_Queue_empty():
		print("Queue is empty")
		return
	front+=1
	data = queue[front]
	queue[front] = None
	if queue[front+1] != None:
		queue = queue[front+1:] + [None]
	front -= 1
	rear -= 1
	return data

SIZE = 5
queue = [ None for _ in range(SIZE) ]
front = rear = -1
if __name__ == "__main__" :
	enQueue("a")
	enQueue("b")
	enQueue("c")
	enQueue("d")
	enQueue("e")
	print(queue)
	deQueue()
	print(queue)
	deQueue()
	print(queue)
	deQueue()
	print(queue)
	deQueue()
	print(queue)
	deQueue()
	print(queue)