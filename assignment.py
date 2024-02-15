# Linked List 응용 문제 2
import random
class Node():
	def __init__(self,data=None):
		self.data = data
		self.link = None
def print_Nodes(start):
	current = start
	if current == None:
		return
	print(current.data, end = " ")
	while current.link != None:
		current = current.link
		print(current.data, end = " ")
	print()

def make_linked_list(num):
	global head
	node = Node(num)
	if head is None:
		head = node
		return
	if head.link == None:
		head.link = node
		return
	current = head
	while current.link is not None:
		current = current.link
		if current.link is None:
			current.link = node
			return

head = None
if __name__ == "__main__":
	for i in range(6):
		make_linked_list(random.randint(1,45))
	print_Nodes(head)