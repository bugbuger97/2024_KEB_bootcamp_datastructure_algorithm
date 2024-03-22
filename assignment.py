class Node:
    def __init__(self,item=None):
        self.item = item
        self.link = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def append(self,item):
        node = Node(item)
        if self.head == None:
            self.head = node
            self.tail = self.head
        elif self.head == self.tail:
            self.tail.link = node
            self.tail = self.tail.link
            self.head.link = self.tail
        else:
            self.tail.link = node
            self.tail = self.tail.link
        self.size += 1
    def print(self): # Q1
        current = self.head
        print(current.item, end=" ")
        while current.link != None:
            current = current.link
            print(current.item,end=" ")
        print()
        return
    def insert(self,idx,item): # Q1
        node = Node(item)
        if self.head == None:
            self.head = node
            self.tail = self.head
        if idx == 0: # 첫번째 노드에 삽입
            node.link = self.head
            self.head = node
        elif idx == self.size: # 마지막 노드에 삽입
            current = self.head
            while current.link != None:
                current = current.link
            current.link = node
            self.tail = node
        else:
            current = self.head
            for _ in range(idx-1):
                current = current.link
            node.link = current.link
            current.link = node
        self.size+=1
    def remove(self,item):
        self.size -= 1
        current = self.head
        if item == self.head.item:
            current = current.link
            self.head.link = None
            self.head = current
        else:
            current = self.head
            while current.item != self.tail.item:
                if (current.link.item == self.tail.item and
                        self.tail.item == item):
                    self.tail = current
                    current.link = None
                    return
                elif current.link.item == item:
                    target = current.link
                    current.link = current.link.link
                    target.link = None
                    return
                current = current.link
            print('해당 노드의 값이 없습니다.')
    def reverse(self):
        current = self.head
        reverse_list = []
        while current.item != self.tail.item:
            reverse_list.append(current.item)
            current = current.link
        reverse_list.append(current.item)
        reverse_list = reverse_list[::-1]
        self.head = None
        self.tail = None
        for i in reverse_list:
            node = Node(i)
            if self.head == None:
                self.head = node
                self.tail = self.head
            elif self.head == self.tail:
                self.tail.link = node
                self.tail = self.tail.link
                self.head.link = self.tail
            else:
                self.tail.link = node
                self.tail = self.tail.link

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.print()
    ll.reverse()
    ll.print()
    print(f'head = {ll.head.item}')
    print(f'tail = {ll.tail.item}')