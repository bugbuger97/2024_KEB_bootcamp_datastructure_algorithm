class Node:
    def __init__(self,item):
        self.item = item
        self.link = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def size(self):
        size = 0
        if self.head == 0:
            return 0
        else:
            current = self.head
            while current != None:
                size += 1
                current = current.link
            return size
    def add(self,idx,item):
        if idx < 0 or self.size() < idx:
            print('idx error')
            return
        current_idx = 0
        node = Node(item)
        if idx == 0:
            node.link = self.head
            self.head = node
            if node.link == None:
                self.tail = self.head
        else:
            current = self.head
            while current is not None and current_idx != idx-1:
                current_idx += 1
                current = current.link
            if current.link == None:
                current.link = node
                self.tail = node
            else:
                node.link = current.link
                current.link = node
    def print(self):
        current = self.head
        while current != None:
            print(current.item, end=" ")
            current = current.link
        print()

    def remove(self,item):
        if self.head.item == item:
            tmp = self.head
            self.head = self.head.link
            tmp.link = None
        elif self.tail.item == item:
            tmp = self.tail
            current = self.head
            while current.link != self.tail:
                current = current.link
            self.tail = current
            current.link = None
        else:
            current = self.head
            while current.link != None:
                if current.link.item == item:
                    tmp = current.link
                    current.link = tmp.link
                    tmp.link = None
                    return
                current = current.link
    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head
        while current:
            next = current.link
            current.link = prev
            prev = current
            current = next
        self.head = prev

if __name__ == '__main__':
    ll = LinkedList()
    ll.add(0,5)
    ll.add(1,3)
    ll.add(2,7)
    ll.add(3,12)
    ll.print()
    ll.remove(7)
    ll.print()
    ll.reverse()
    ll.print()