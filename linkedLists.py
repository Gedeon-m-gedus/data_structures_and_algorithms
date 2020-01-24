class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None

class myList():
    def __init__(self,head=None):
        self.head = head
    
    def add(self, data):        
        node = Node(data)
        if self.head == None:
            self.head = node
            return 
        cur_pos = self.head
        while cur_pos.next != None:
            cur_pos = cur_pos.next
        cur_pos.next = node
    def printlist(self):
        cur_pos = self.head
        while cur_pos.next != None:
            print(cur_pos.data)
            cur_pos = cur_pos.next
        print(cur_pos.data)
    def insert(self,pos,data):
        k = 1
        node = Node(data)
        cur_pos = self.head
        while k < pos:
            cur_pos = cur_pos.next
            k+=1
        hook = cur_pos.next
        cur_pos.next = node
        node.next = hook
    def delete(self,pos):
        k = 1
        cur_pos = self.head
        while k < pos:
            cur_pos = cur_pos.next
            k+=1
        hook = cur_pos.next
        hook2 = hook.next
        cur_pos.next = hook2

l = myList()
l.add(3)
l.add(45)
#l.printlist()
l.add(3)
l.add(5)
l.add(1)
l.add(4)
l.printlist()
l.insert(2,400)
l.printlist()
l.delete(2)
l.printlist()
    
