# 4-2
class Node():
	def __init__(self):
		self.data = None
		self.link = None
def print_Nodes(start):
	current = start
	if current == None:
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()
def make_Simple_Linked_List(String_Number):
	global head, current, pre
	print_Nodes(head)
	node = Node()
	node.data = String_Number
	if head == None:
		head = node
		return
	if head.data[1] > String_Number[1]:
		node.link = head
		head = node
		return
	current = head
	while current.link != None:
		pre = current
		current = current.link
		if current.data[1] > String_Number[1]:
			pre.link = node
			node.link = current
			return
	current.link = node

head, current, pre = None, None, None
data_array = [["가", 5], ["나", 4], ["다", 2], ["라", 3], ["마", 1]]
if __name__ == "__main__":
	for data in data_array:
		make_Simple_Linked_List(data)
	print_Nodes(head)