'''
binary tree

binary tree traversal -> 재귀 사용

전위 순회
1. current 노드 데이터 처리
2. left 자식 트리로 이동
3. right 자식 트리로 이동

중위 순회
1. left 자식 트리로 이동
2. current 노드 데이터 처리
3. right 자식 트리로 이동

후위 순회
1. left 자식 트리로 이동
2. right 자식 트리로 이동
3. current 노드 데이터 처리
'''
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

if __name__ == "__main__":
	node1 = tree_node('첫째')
	node2 = tree_node('둘째')
	node3 = tree_node('셋째')
	node4 = tree_node('넷째')
	node5 = tree_node('다섯째')
	node6 = tree_node('여섯째')
	node7 = tree_node('일곱째')
	node1.left = node2
	node1.right = node3
	node2.left = node4
	node2.right = node5
	node3.left = node6
	node3.right = node7
	print(node1.data)
	print(node1.left.data,node1.right.data)
	print(node1.left.left.data,node1.left.right.data,node1.right.left.data,node1.right.right.data)
	'''
	                 첫째
	        둘째			     셋째
	    넷째	   다섯째    여섯째    일곱째
	'''
	print(f'preorder : ', end = '')
	preorder(node1)
	print('끝')

	print(f'inorder : ', end='')
	inorder(node1)
	print('끝')

	print(f'postorder : ', end='')
	postorder(node1)
	print('끝')