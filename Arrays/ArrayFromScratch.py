"""
This definitely is not a proper implementation of array. This is implementation of 'list'.
"""


class MyArray:

    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data.get(index)

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

        return self.length

    def pop(self):
        if self.data:
            last_index = self.length - 1
            item = self.data[last_index]
            del self.data[last_index]
            self.length -= 1
            return item
        raise IndexError("pop from an empty array")

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    def delete(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Invalid index")

        if index == self.length - 1:
            item = self.pop()
            return item
        else:
            return self.shift_items(index)

    def shift_items(self, index):
        item = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

        del self.data[self.length - 1]
        self.length -= 1
        return item

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    arr = MyArray()
    print(arr.get(0))
    arr.push(1)
    arr.push(3)
    arr.push(2)
    arr.push(4)
    arr.push(3)
    arr.push(5)

    print(arr)
    arr.delete(1)
    arr.delete(2)
    arr.delete(3)

    print(arr)
    print(arr.length)
