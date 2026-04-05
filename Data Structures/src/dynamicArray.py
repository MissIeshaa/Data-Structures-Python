# dynamicArray.py
# A simple implementation of a dynamic array

class dynamicArray:
    def __init__(self):
        self.array = [None] * 1
        self.capacity = 1
        self.length = 0

    def append(self, value):
        if self.length == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.length] = value
        self.length += 1

    def _resize(self, newCapacity):
        newArray = [None] * newCapacity
        for i in range(self.length):
            newArray[i] = self.array[i]
        self.array = newArray
        self.capacity = newCapacity

    def _getitem_(self, index):
        if 0 <= index <= self.length:
            return self.array[index]
        raise IndexError("Index out of range")

    def __len__(self):
        return self.length
