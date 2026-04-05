# queue.py
# Queue using Python list

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, param):
        pass

