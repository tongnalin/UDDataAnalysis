#!/usr/bin/env python2

class FibIterable(object):
    def __init__(self, iLast = 1, iSecondLast = 0, iMax = 100):
        self.iLast = iLast
        self.iSecondLast = iSecondLast
        self.iMax = iMax

    def __iter__(self):
        return self

    def next(self):
        iNext = self.iLast + self.iSecondLast
        if iNext > self.iMax:
            raise StopIteration()
        self.iSecondLast = self.iLast
        self.iLast = iNext
        return iNext

o = FibIterable()
for i in o:
    print i
