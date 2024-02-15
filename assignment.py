class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None
def print_Nodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()
def delete_Node(deleteData):
    global head, current, pre
    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        print("첫 노드가 삭제됨")
        return
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            print("중간 노드가 삭제됨")
            return
    else:
        print("삭제된 노드가 없음")

head, current, pre = None, None, None
dataArray = ["가", "나", "다", "라", "마"]

if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
    print_Nodes(head)
    delete_Node("가")
    print_Nodes(head)
    delete_Node("다")
    print_Nodes(head)
    delete_Node("라")
    print_Nodes(head)
    delete_Node("라")
    print_Nodes(head)