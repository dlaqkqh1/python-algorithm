class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __getitem__(self, index):
        time = self.start + index
        self.hour = int(time / 3600 % 24)
        self.minute = int(time / 60 % 60)
        self.second = int(time % 60)
        if index < self.stop - self.start:
            return "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.minute, self.second)
        else:
            raise IndexError
            
start, stop, index = map(int, input().split())
 
for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')