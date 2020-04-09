class Node:
    def __init__(self, item):
        self.item = item
        self.next_link = None
 
class Linked_List:
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None
 
    def change(self, index, item):
        temp = self.head
        for _ in range(index):
            temp = temp.next_link
        temp.item = item
 
    def append(self, item):
        self.length += 1
        node = Node(item)
        if self.head != None:
            self.tail.next_link = node
        else:
            self.head = node
        self.tail = node

    def get(self, index):
        if self.tail == None:
            return -1
        if index >= self.length:
            return -1
        temp = self.head
        for _ in range(index):
            temp = temp.next_link
        return temp.item
 
    def insert(self, index, item):
        node = Node(item)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next_link
            node.next_link = temp.next_link
            temp.next_link = node
        self.length += 1
 
    def pop(self,index):
        temp = self.head
        for _ in range(index-1):
            temp = temp.next_link
        temp.next_link = temp.next_link.next_link
        self.length -=1
 
for t in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    temp = input().split()
    linked_list = Linked_List()
    for i in temp:
        linked_list.append(i)
    for _ in range(M):
        method = input().split()
        if method[0] == 'I':
            linked_list.insert(int(method[1]),int(method[2]))
        elif method[0] == 'D':
            linked_list.pop(int(method[1]))
        else:
            linked_list.change(int(method[1]), int(method[2]))
    print('#{} {}'.format(t, linked_list.get(L)))