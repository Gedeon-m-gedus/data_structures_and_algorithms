
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

#### General Review
The basics of data structures form the foundation of computer science and programming. Here are some fundamental data structures:

##### Arrays:
- An ordered collection of elements where each element can be accessed using an index.
- Operations include insertion, deletion, and access.
- Arrays have constant time access to elements (O(1)), but insertion and deletion may be O(n) in the worst case.

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

##### 1. Trees (Binary Search, Red-Black, binary, BST, AVL, 2-3, splay)

