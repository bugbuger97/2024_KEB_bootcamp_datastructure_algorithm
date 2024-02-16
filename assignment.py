"""
Circle Linked List
마지막 노드의 링크가 None이 아니라 head를 가리킴.
오버헤드 발생 x
"""
# Circle Linked List 응용 1
import random
class Node():
	def __init__(self,data=None):
		self.data = data
		self.link = None
def print_Node(start):
	current = start
	if current.link == None:
		return
	print(f"{current.data[0]}편의점,", end = " ")
	print(f"거리 : {(current.data[1] ** 2 + current.data[2] ** 2) ** 0.5}")
	while current.link != start:
		current = current.link
		print(f"{current.data[0]}편의점,", end = " ")
		print(f"거리 : {(current.data[1]**2 + current.data[2]**2)**0.5}")
	print()
def make_circle_linked_list(data):
	global head
	node = Node(data)
	if head is None:
		head = node
		node.link = head
		return
	if head.link == head:
		head.link = node
		node.link = head
		return
	current = head
	while current.link != head:
		current = current.link
		if current.link == head:
			current.link = node
			node.link = head
			return

def insert_Node(find_data,insert_data):
	global head
	if head.data == find_data:
		node = Node(insert_data)
		node.link = head
		current = head
		while current.link != head:
			current = current.link
		current.link = node
		head = node
		return
	current = head
	while current.link != head:
		pre = current
		current = current.link
		if current.data == find_data:
			node = Node(insert_data)
			node.link = current
			pre.link = node
			return
	node = Node()
	node.data = insert_data
	current.link = node
	node.link = head

head = None
num_list = [i for i in range(10)]
arr = random.sample(num_list,10)
x = [random.randint(1,100) for i in range(10)]
y = [random.randint(1,100) for i in range(10)]
if __name__ == "__main__":
	for i in range(10):
		make_circle_linked_list((chr(arr[i]+65),x[i],y[i]))
	print_Node(head)
