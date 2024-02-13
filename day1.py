# 삽입, 삭제할 때 : 링크드 리스트 유리
# 검색할 때 : 배열, 벡터가 유리

class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None
def print_nodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()
def make_simple_linked_list(number) :
	global head, current, pre
	print_nodes(head)
	node = Node()
	node.data = number
	if head == None :
		head = node
		return
	if head.data[1] < number[1] :
		node.link = head
		head = node
		return
	current = head
	while current.link != None :
		pre = current
		current = current.link
		if current.data[1] < number[1]:
			pre.link = node
			node.link = current
			return
	current.link = node

head, current, pre = None, None, None
dataArray = [["가", "1"], ["나", "2"], ["다", "3"], ["라", "4"], ["마", "5"]]

print(globals())
if __name__ == "__main__" :
	for data in dataArray :
		make_simple_linked_list(data)
	print_nodes(head)