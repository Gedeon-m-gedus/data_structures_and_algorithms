class Node():
    def __init__(self,data):
        self.data = data
        self.next = next

class myQueue():
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail
    
    def enqueue(self,data):
        node = Node(data)
        self.head, node.next = node, self.head
    def dequeue(self):
        pos = self.head
        while pos.next!=None:
            prev_pos = pos
            pos = pos.next
        prev_pos.next = None
        return pos.data
    
    def printQueue(self):
        if self.head == None: return
        cur_pos = self.head
        l = []
        while cur_pos.next != None:
            l.append(cur_pos.data)
            cur_pos = cur_pos.next
        l.append(cur_pos.data)
        return l
q = myQueue()
q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
print(q.printQueue())
print(q.dequeue())
print(q.printQueue())
