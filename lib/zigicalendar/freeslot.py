from .timeslot import Timeslot
from .date import Date
import json


class Freeslot(Timeslot):
    def __init__(self,start:Date,end:Date):
        self.type = "free"
        super().__init__(start,end)

    def __repr__(self):
        return "*Freetime from %s to %s" % (self.start,self.end)

    def toJson(self):
        return {
            'type' : 'freeslot',
            'startTime': str(self.start),
            'endTime': str(self.end)
        }