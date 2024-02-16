# double linked list 응용 2
import random
class Node():
	def __init__(self,data=None):
		self.left = None
		self.data = data
		self.right = None
def print_right_Node(start):
	current = start
	if current.right == None:
		return
	print(current.data, end=" ")
	while current.right != None:
		current = current.right
		print(current.data, end = " ")
	print()
def print_left_Node(start):
	current = start
	if current.right == None:
		return
	while current.right != None:
		current = current.right
	print(current.data, end=" ")
	while current.left != None:
		current = current.left
		print(current.data, end = " ")
	print()
def make_double_linked_list(data):
	global head
	node = Node(data)
	if head == None:
		head = node
		return
	if head.right == None and head.left == None:
		head.right = node
		node.left = head
		return
	current = head
	while current.right != None:
		current = current.right
		if current.right == None:
			current.right = node
			node.left = current
			return

head = None
arr = [chr(i+65) for i in range(5)]
if __name__ == "__main__":
	for i in arr:
		make_double_linked_list(i)
	print_right_Node(head)
	print_left_Node(head)