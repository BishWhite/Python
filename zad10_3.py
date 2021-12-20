class Stack:
    

    def __init__(self, size):
        if not isinstance(size, int):
            raise ValueError('rozmiar tylko typu int')
        if size <= 0:
            raise ValueError('rozmiar >= 0')
        self.items = size * [None]
        self.exists = size * [0]
        self.size = size
        self.index = 0

    def __str__(self):
        return str(self.items[:self.index])

    def is_empty(self):

        return self.index == 0

    def is_full(self):

        return self.index == self.size

    def push(self, item):

        if not 0 <= item <= self.size-1:
            raise ValueError(
                'Wartość musi być liczbą całkowitą z przedziału [0, {}]'.format(self.size-1))
        if self.exists[item]:
            return
        self.items[self.index] = item
        self.exists[item] = 1
        self.index += 1

    def pop(self):

        if self.is_empty():
            raise Exception('Stos jest pusty')
        self.index -= 1
        item = self.items[self.index]
        self.items[self.index] = None
        self.exists[item] = 0
        return item