class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add(self,data):
        if self.data:
            if data > self.data:
                if self.left is not None:
                    self.left.add(data)
                else:
                    self.left = Node(data)
            else:
                if self.right is not None:
                    self.right.add(data)
                else:
                    self.right = Node(data)

        else:
            self.data = Node(data)
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    
    def search(self,data):
        if self.data<data:
            if self.left is None:
                return print('Not found')
            return self.left.search(data)
            
        elif self.data>data:
            if self.right is None:
                return print('Not found')
            return self.right.search(data)
            
        else:
            return print('Number found')

root = Node(50)
root.add(23)
root.add(93)
root.add(203)
root.add(2)
root.add(9)
root.add(20)
root.printTree()
root.search(2)
root.search(0)
#root.printTree()