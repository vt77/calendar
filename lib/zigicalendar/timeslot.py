
from .date import Date

class Timeslot(object):

    def __init__(self,start:Date,end:Date):
        self.start = start
        self.end = end
    
    def __gt__(self,other):
        return self.start.minutes() > other.start.minutes()
    
    def __lt__(self,other):
        return self.start.minutes() < other.start.minutes()

    def __add__(self,other):
        if other.end > self.end : 
                self.end = other.end
        return self