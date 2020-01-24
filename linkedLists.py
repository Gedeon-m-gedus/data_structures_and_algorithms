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
l = myList()
l.add(3)
l.add(45)
l.printlist()
l.add(3)
l.add(5)
l.add(1)
l.add(4)
l.printlist()
    
