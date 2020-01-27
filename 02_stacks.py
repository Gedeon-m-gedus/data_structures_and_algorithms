class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class myStack():
    def __init__(self,head = None):
        self.head = head
    def push(self,data):
        node = Node(data)
        # cur_pos = self.head
        self.head, node.next = node, self.head
        # next_pos = cur_pos.next
        # cur_pos = node
        # node.next = next_pos
    def printStack(self):
        cur_pos = self.head
        l = []
        while cur_pos.next != None:
            l.append(cur_pos.data)
            cur_pos = cur_pos.next
        l.append(cur_pos.data)
        return l
    def pop(self):
        d = self.head.data
        self.head = self.head.next
        return d
m = myStack()
m.push(7)
m.push(0)
m.push(9)
print(m.printStack())
print(m.pop())
print(m.printStack())