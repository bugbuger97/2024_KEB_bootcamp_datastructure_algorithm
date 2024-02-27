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
def delete_tree_node(del_data):
	global root
	current = root
	parent = None
	while True:
		if del_data == current.data:
			if current.left == None and current.right == None:
				if parent.left == current:
					parent.left = None
				else:
					parent.right = current.left
				del(current)
			elif current.left != None and current.right == None:
				if parent.left == current:
					parent.left = None
				else:
					parent.right = current.left
				del (current)
			elif current.left == None and current.right != None:
				if parent.left == current:
					parent.left = None
				else:
					parent.right = current.left
				del (current)
			print(f'{del_data} is deleted')
			break
		elif del_data < current.data:
			if current.left == None:
				print(f"{del_data} don't exist in the tree")
				break
			parent = current
			current = current.left
		else:
			if current.right == None:
				print(f"{del_data} don't exist in the tree")
				break
			parent = current
			current = current.right

root = None
arr = ['바', '라', '마', '아', '가', '타']
if __name__ == "__main__":
	'''
	           바
	    라			  마
	가        	 아         타
	'''
	make_tree(arr)
	preorder(root)
	print("끝")
	print()
	delete_tree_node('아')
	preorder(root)
	print("끝")