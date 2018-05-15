
class Numberline(object):
    """Numberline where intervals can be added, and total amt of time returned """

    def __init__(self):
        self.intervals = set()

    def add_interval(self, start, end):
        for i in range(start, end):
            self.intervals.add(i)

    def total_time(self):
        return len(self.intervals)


x = Numberline()
x.add_interval(2, 4)
x.add_interval(3, 5)
x.add_interval(6, 7)

print x.total_time()
