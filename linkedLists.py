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
        l = []
        while cur_pos.next != None:
            l.append(cur_pos.data)
            cur_pos = cur_pos.next
        l.append(cur_pos.data)
        return l
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
    def lenght(self):
        l = 1
        cur_pos = self.head
        while cur_pos.next != None:
            cur_pos = cur_pos.next
            l += 1
        return l
    def maxi(self):
        l = self.printlist()
        return max(l)

l = myList()
l.add(3)
l.add(45)
#l.printlist()
l.add(3)
l.add(5)
l.add(1)
l.add(4)
print(l.printlist())
print(l.lenght())
l.insert(2,400)
print(l.printlist())
print(l.maxi())
print(l.lenght())
l.delete(2)
print(l.printlist())
print(l.lenght())
l.delete(2)
print(l.printlist())
print(l.lenght())
print(l.maxi())
    
