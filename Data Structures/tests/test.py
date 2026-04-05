# test.py

from src.dynamicArray import dynamicArray
from src.linkedList import linkedList
from src.stack import Stack
from src.queue import Queue

# test dynamicArray

arr = dynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)
print("Dynamic Array Length: ", len(arr))

# test linkedList

ll = linkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print("Linked List:")
ll.display()

# test stack

stack = Stack()
stack.push("A")
stack.push("B")
print("Stack pop: ", stack.pop())

# test queue

queue = Queue()
queue.enqueue("X")
queue.enqueue("Y")
print("Queue dequeue: ", queue.dequeue())
