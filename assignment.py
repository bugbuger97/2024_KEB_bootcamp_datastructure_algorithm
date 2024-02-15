"""
Linked list
[data, link] -> [data, link] -> [data, link]
노드들이 물리적으로 떨어져 있지만 link로 이어져 있어 마치 선형 리스트와 비슷하게 이어져 있음.

node insert
1. 삽입할 새 노드 생성
2. 새 노드의 링크에 다음에 들어갈 node를 연결 시킴
3. 전 node의 링크를 새 노드에 연결 시킴

node delete
1. 삭제할 노드의 전 노드의 링크를 삭제할 노드의 후 노드에 바로 연결시킴
2. 삭제할 노드를 삭제 시킴
"""

# 4-1
class Node():
    def __init__(self,data=None):
        self.data = data
        self.link = None
    def Link(self,link):
        self.link = link
def print_linked_list():
    current = head
    if current == None:
        return
    print(current.data, end=" -> ")
    while current.link is not None:
        current = current.link
        print(current.data, end = " -> ")
    print(current.link)

head = Node('head')
if __name__ == "__main__":
    node1 = Node("가")
    node2 = Node("나")
    node3 = Node("다")
    node4 = Node("라")
    node5 = Node("마")
    node6 = Node("바")
    node7 = Node("사")
    head.Link(node1)
    node1.Link(node2)
    node2.Link(node3)
    node3.Link(node4)
    node4.Link(node5)
    node5.Link(node6)
    node6.Link(node7)
    print_linked_list()