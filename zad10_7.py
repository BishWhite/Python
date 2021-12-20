class PriorityQueue:

    def __init__(self, cmpf=lambda a, b: (a > b) - (a < b)):  
        self.items = []
        self.cmpf = cmpf

    def __str__(self):
        return str(self.items)

    def is_empty(self):

        return not self.items

    def insert(self, item):

        self.items.append(item)

    def remove(self):
        
        max = 0
        for i in range(1, len(self.items)):
            if self.cmpf(self.items[i], self.items[max]) == 1:
                max = i
        return self.items.pop(max)