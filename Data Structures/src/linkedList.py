# linkedList.py
# singly linked list implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        newNode = Node(value)

        if not self.head:
            self.head = newNode
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = newNode

    def display(self):
        current = self.head
        values = []

        while current:
            values.append(str(current.value))
            current = current.next

        print(" -> ".join(values))
