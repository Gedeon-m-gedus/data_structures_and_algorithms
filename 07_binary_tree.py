class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add(self,data):
        if self.data:
            if self.data < data:
                if self.left is not None:
                    self.left.add(data):
                else:
                    self.left = Node(data)
            else:
                if self.right is not None:
                    self.right.add(data)
                else:
                    self.right = Node(data)

        else:
            self.data = Node(data)