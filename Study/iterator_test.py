class MultipleIterator:
    def __init__(self, stop, multiple):
        self.stop = stop
        self.multiple = multiple
        self.current = 1
                                 
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.current * self.multiple < self.stop:
            r = self.current * self.multiple
            self.current += 1
            return r
        else:
            raise StopIteration
                                                     
 
for i in MultipleIterator(20, 3):
    print(i, end=' ')
 
print()
for i in MultipleIterator(30, 5):
    print(i, end=' ')