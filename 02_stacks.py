class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None
class myStack():
    def __init__(self,head = None):
        self.head = head
    def push(self,data):
        node = Node(data)
        #self.head, node.next = node, self.head
        cur_pos = node
        node.next = self.head
        self.head=node
    def printStack(self):
        if self.head == None: return
        cur_pos = self.head
        l = []
        while cur_pos.next != None:
            l.append(cur_pos.data)
            cur_pos = cur_pos.next
        l.append(cur_pos.data)
        return l
    def pop(self):
        if self.head == None: return
        d = self.head.data
        self.head = self.head.next
        return d
m = myStack()
m.push(7)
m.push(0)
m.push(9)
m.push(19)
print(m.printStack())
print(m.pop())
print(m.printStack())
print(m.pop())
print(m.pop())
print(m.pop())
print(m.pop())
print(m.pop())
print(m.printStack())
