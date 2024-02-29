import os
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

def duplicates():
	global arr
	stack = []
	for i in arr:
		if arr.count(i) > 1 and i not in stack:
			stack.append(i)
	return stack

def list_files_in_directory(directory):
	arr = []
	for root, dirs, files in os.walk(directory):
		for file in files:
			file_path = os.path.join(root)
			arr.append(file_path)
	return arr

root = None
target_directory = f"C:/Users/user/Desktop"
arr = list_files_in_directory(target_directory)
if __name__ == "__main__":
	print(f'{target_directory} 및 그 하위 디렉토리의 중복된 파일 목록 --> ')
	print(duplicates())