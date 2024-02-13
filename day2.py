# circle linked list
import random
class Node() :
    def __init__ (self):
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link is not start:
        current = current.link
        print(current.data, end=' ')
    print()

def insert_node(findData, insertData):
	global head, current, pre

	if head.data == findData :
		node = Node()
		node.data = insertData
		node.link = head
		last = head
		while last.link is not head:
			last = last.link
		last.link = node
		head = node
		return
	current = head
	while current.link is not head:
		pre = current
		current = current.link
		if current.data == findData:
			node = Node()
			node.data = insertData
			node.link = current
			pre.link = node
			return
	node = Node()
	node.data = insertData
	current.link = node
	node.link = head

def minus_node(start):
    odd_cnt = 0
    even_cnt = 0
    current = start
    if current.link == None:
        return
    while current.link is not start:
        current = current.link
        if current.data%2 == 0:
            even_cnt+=1
        else:
            odd_cnt+=1
    if even_cnt > odd_cnt:
        flag = 0
    else:
        flag = 1
    current = start
    while current.link is not start:
        if current.data%2 == flag:
            current.data *= -1
        print(current.data, end=' ')
        current = current.link
    print()

# 전역 변수
head, current, pre = None, None, None
dataArray = [random.randint(1,100) for i in range(10)]
# 메인문
if __name__ == "__main__" :
    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    # node 연결 -> circle linked list
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
    print_nodes(head)
    minus_node(head)