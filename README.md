
# Data structures and algorithms

A review of the common Data structures and algorithms

#### Review Outline
- Trees (Binary Search, Red-Black, binary, BST, AVL, 2-3, splay)
- Graphs (un/directed, un/weighted)
- Hash Tables
- Heaps
- Linked Lists (singly linked, doubly linked, circularly linked)
- Stacks
- Queues (inc. Priority)
- Arrays
- Array Lists

## General Review
The basics of data structures form the foundation of computer science and programming. Here are some fundamental data structures:

##### Arrays:
- An ordered collection of elements where each element can be accessed using an index.
- Operations include insertion, deletion, and access.
- Arrays have constant time access to elements `(O(1))`, but insertion and deletion may be `O(n)` in the worst case.

```python

my_array = [1, 2, 3, 4, 5]
print(my_array[2])
my_array.append(6)
del my_array[1]
print(my_array)

```

##### Linked Lists:
- A collection of nodes where each node contains data and a reference (or link) to the next node in the sequence.
- Operations include insertion, deletion, and traversal.
- Linked lists allow for dynamic memory allocation but have slower access times compared to arrays.

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next_node = node2
node2.next_node = node3

current_node = node1
while current_node:
    print(current_node.data)
    current_node = current_node.next_node

```

##### Stacks:
- A Last-In-First-Out (LIFO) data structure where elements are added and removed from the same end (the top).
- Operations include push (add an element) and pop (remove the top element).
- Stacks are used for managing function calls, expression evaluation, and undo mechanisms.

```python
my_stack = []
my_stack.append(1)
my_stack.append(2)
my_stack.append(3)
popped_element = my_stack.pop()
print(popped_element)

```

##### Queues:
- A First-In-First-Out (FIFO) data structure where elements are added at the rear and removed from the front.
- Operations include enqueue (add an element) and dequeue (remove the front element).
- Queues are used in scenarios like task scheduling and breadth-first search in graphs.

```python
from collections import deque

my_queue = deque()
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)
dequeued_element = my_queue.popleft()
print(dequeued_element)

```

##### Trees:
- A hierarchical data structure with a root element and subtrees of children with a parent-child relationship.
- Binary Trees: Each node has at most two children (left and right).
- Binary Search Trees (BST): A binary tree with the property that the left subtree of a node contains only nodes with keys less than the node's key, and the right subtree contains only nodes with keys greater than the node's key.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

```

##### Graphs:
- A collection of nodes (vertices) and edges connecting these nodes.
- Directed Graphs: Edges have a direction.
- Undirected Graphs: Edges have no direction.
- Graphs can be represented using adjacency matrices or adjacency lists.

```python
my_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

```

##### Heaps:
- A specialized tree-based data structure that satisfies the heap property.
- Max Heap: The value of each node is greater than or equal to the values of its children.
- Min Heap: The value of each node is less than or equal to the values of its children.
- Heaps are commonly used for implementing priority queues.

```python
import heapq

my_heap = [3, 1, 4, 1, 5, 9, 2]
heapq.heapify(my_heap)
heapq.heappush(my_heap, 6)
min_element = heapq.heappop(my_heap)
print(min_element)

```

##### Hash Tables:
- A data structure that maps keys to values using a hash function to compute an index into an array of buckets.
- Allows for efficient insertion, deletion, and retrieval of data.
- Hash collisions (different keys hashing to the same index) need to be handled.

```python
my_hash_table = {}
my_hash_table['one'] = 1
my_hash_table['two'] = 2
my_hash_table['three'] = 3
print(my_hash_table['two'])

```

## Trees (Binary Search, Red-Black, binary, BST, AVL, 2-3, splay)
Trees are hierarchical data structures composed of nodes connected by edges. Each node in a tree has a parent and zero or more children. There are various types of trees, each with its own rules and properties. Let's explore some commonly used types of trees:

##### Binary Tree:
- A tree in which each node has at most two children, usually referred to as the left child and the right child.
- Nodes in a binary tree are often used to represent expressions, hierarchical structures, or binary search trees.
```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
```

##### Binary Search Tree (BST):
- A binary tree with the property that the left subtree of a node contains only nodes with keys less than the node's key, and the right subtree contains only nodes with keys greater than the node's key.
- Allows for efficient search, insertion, and deletion operations with an average time complexity of O(log n), where n is the number of nodes.
```python
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Example usage:
bst_root = None
keys = [5, 3, 7, 2, 4, 6, 8]

for key in keys:
    bst_root = insert(bst_root, key)

```

##### AVL Tree:
- A self-balancing binary search tree where the height difference between the left and right subtrees of any node (called the balance factor) is at most 1.
- Balancing is achieved through rotations (single and double) to maintain the logarithmic height and ensure efficient operations.
- Ensures that the time complexity of search, insert, and delete operations remains O(log n).
```python
class AVLNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1

def height(node):
    if not node:
        return 0
    return node.height

def balance_factor(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y

def insert_avl(root, key):
    if not root:
        return AVLNode(key)

    if key < root.val:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)

    root.height = 1 + max(height(root.left), height(root.right))

    balance = balance_factor(root)

    # Left Left Case
    if balance > 1 and key < root.left.val:
        return rotate_right(root)

    # Right Right Case
    if balance < -1 and key > root.right.val:
        return rotate_left(root)

    # Left Right Case
    if balance > 1 and key > root.left.val:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    # Right Left Case
    if balance < -1 and key < root.right.val:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root

# Example usage:
avl_root = None
keys = [5, 3, 7, 2, 4, 6, 8]

for key in keys:
    avl_root = insert_avl(avl_root, key)
```

##### Red-Black Tree:
- Another self-balancing binary search tree that uses a coloring scheme to maintain balance.
- Each node in the tree is assigned a color (either red or black), and certain rules are enforced to ensure balance during insertions and deletions.
- Provides O(log n) time complexity for search, insert, and delete operations.
```python
class NodeRB:
    def __init__(self, key, color='Red'):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color

class RedBlackTree:
    def __init__(self):
        self.NIL = NodeRB(0, color='Black')  # Sentinel node representing NIL
        self.root = self.NIL

    def insert(self, key):
        new_node = NodeRB(key)
        new_node.left = self.NIL
        new_node.right = self.NIL
        new_node.parent = self.NIL

        current = self.root
        parent = None

        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = 'Black'
            return

        if new_node.parent.parent is None:
            return

        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node.parent.color == 'Red' and node != self.root:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left  # parent's sibling
                if uncle.color == 'Red':
                    node.parent.color = 'Black'
                    uncle.color = 'Black'
                    node.parent.parent.color = 'Red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'Black'
                    node.parent.parent.color = 'Red'
                    self.left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right
                if uncle.color == 'Red':
                    node.parent.color = 'Black'
                    uncle.color = 'Black'
                    node.parent.parent.color = 'Red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'Black'
                    node.parent.parent.color = 'Red'
                    self.right_rotate(node.parent.parent)

        self.root.color = 'Black'

    def left_rotate(self, node):
        y = node.right
        node.right = y.left
        if y.left != self.NIL:
            y.left.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.left = node
        node.parent = y

    def right_rotate(self, node):
        y = node.left
        node.left = y.right
        if y.right != self.NIL:
            y.right.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.right = node
        node.parent = y

    def inorder_traversal(self, node):
        if node != self.NIL:
            self.inorder_traversal(node.left)
            print(f'({node.key}, {node.color})', end=' ')
            self.inorder_traversal(node.right)

# Example usage:
rb_tree = RedBlackTree()
keys = [5, 3, 7, 2, 4, 6, 8]

for key in keys:
    rb_tree.insert(key)

rb_tree.inorder_traversal(rb_tree.root)

```

##### 2-3 Tree:
- A type of search tree where each node can have 2 or 3 children.
- Designed to be perfectly balanced, ensuring that all leaf nodes are at the same level.
- Used in the implementation of B-trees, which are often employed in file systems and databases.
```python
class Node23:
    def __init__(self, key1, key2=None):
        self.key1 = key1
        self.key2 = key2
        self.child_left = None
        self.child_middle = None
        self.child_right = None

# Example usage:
node1 = Node23(1)
node2 = Node23(2)
node3 = Node23(3)

node1.child_left = node2
node1.child_middle = node3
```

##### Splay Tree:
- A self-adjusting binary search tree where recently accessed elements are moved to the root to improve future access times.
- The idea is to bring frequently accessed nodes closer to the root, reducing access time for those nodes.
- No explicit balancing is done; the tree is "splayed" based on access patterns.
```python
class SplayNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def splay(root, key):
    if not root or root.key == key:
        return root

    if key < root.key:
        if not root.left:
            return root

        # Zig-Zig (Left Left)
        if key < root.left.key:
            root.left.left = splay(root.left.left, key)
            root = rotate_right(root)

        # Zig-Zag (Left Right)
        elif key > root.left.key:
            root.left.right = splay(root.left.right, key)
            if root.left.right:
                root.left = rotate_left(root.left)

        return rotate_right(root)

    else:
        if not root.right:
            return root

        # Zag-Zag (Right Right)
        if key > root.right.key:
            root.right.right = splay(root.right.right, key)
            root = rotate_left(root)

        # Zag-Zig (Right Left)
        elif key < root.right.key:
            root.right.left = splay(root.right.left, key)
            if root.right.left:
                root.right = rotate_right(root.right)

        return rotate_left(root)

def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    return x

def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

# Example usage:
splay_root = None
keys = [5, 3, 7, 2, 4, 6, 8]

for key in keys:
    splay_root = splay(splay_root, key)
```
