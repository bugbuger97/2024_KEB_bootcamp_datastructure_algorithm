class tree_node():
	def __init__(self,data=None):
		self.left = None
		self.data = data
		self.right = None
def preorder(node):
	if node == None:
		return
	else:
		print(node.data, end = ' -> ')
		preorder(node.left)
		preorder(node.right)
def inorder(node):
	if node == None:
		return
	else:
		inorder(node.left)
		print(node.data, end=' -> ')
		inorder(node.right)
def postorder(node):
	if node == None:
		return
	else:
		postorder(node.left)
		postorder(node.right)
		print(node.data, end = " -> ")
def make_tree(arr):
	global root
	node = tree_node(arr[0])
	root = node
	for data in arr[1:]:
		node = tree_node(data)
		current = root
		while True:
			if data < current.data:
				if current.left == None:
					current.left = node
					break
				current = current.left
			else:
				if current.right == None:
					current.right = node
					break
				current = current.right

def Remove_duplicates(arr):
	cnt = 0
	arr_end = len(arr) - 1
	temp = arr[0]
	stack = [arr[0]]
	for i in arr:
		cnt += 1
		if i in stack:
			continue
		else:
			stack.append(i)
	return stack


root = None
arr = ['레쓰비캔 커피', '레쓰비캔 커피', '레쓰비캔 커피', '도시락', '도시락', '삼각김밥','레쓰비캔 커피',
	   '도시락', '코카콜라','삼다수','레쓰비캔 커피','레쓰비캔 커피','레쓰비캔 커피','츄파춥스','츄파춥스',
	   '레쓰비캔 커피','코카콜라','츄파춥스','삼각김밥','코카콜라']
if __name__ == "__main__":
	print(f'오늘 판매된 물건(중복O) --> {arr}\n')
	result=Remove_duplicates(arr)
	make_tree(result)
	print('이진 탐색 트리 구성 완료!\n')
	print('오늘 판매된 종류(중복 X) --> ',end='')
	preorder(root)
	print("끝")