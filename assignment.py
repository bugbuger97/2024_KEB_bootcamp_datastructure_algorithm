# Linked List 응용 문제 1
class Node():
	def __init__(self,data=None):
		self.data = data
		self.link = None
def print_Nodes(start):
	current = start
	if current == None:
		return
	print(current.data, end = " -> ")
	while current.link != None:
		current = current.link
		print(current.data, end = " -> ")
	print(current.link)
def make_linked_list(name,email):
	global head, current, pre
	node = Node([name,email])
	if head == None:
		head = node
		return print_Nodes(head)
	if head.data[0] > node.data[0]:
		node.link = head
		head = node
		return print_Nodes(head)
	if head.link is None and head.data[0] < node.data[0]:
		head.link = node
		return print_Nodes(head)
	else:
		current = head
		while current.link is not None:
			pre = current
			current = current.link
			if current.data[0] > node.data[0]:
				pre.link = node
				node.link = current
				return print_Nodes(head)
		current.link = node
		return print_Nodes(head)

head, current, pre = None, None, None
if __name__ == "__main__":
	while True:
		name = input("이름 : ")
		if name == "0":
			break
		email = input("이메일 : ")
		make_linked_list(name, email)