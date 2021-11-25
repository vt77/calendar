
import logging
logger = logging.getLogger(__name__)

from .timeslot import Timeslot
from .date import Date


class Meeting(Timeslot):
    def __init__(self,person:str,subject:str,start:Date,end:Date):
        self.type = "meeting"
        self.person = person
        self.subject = subject
        super().__init__(start,end)
        logger.debug("[MEETING]Created %s" % self )

    def __repr__(self):
        return "Meeting %s for %s from %s to %s" % (self.subject,self.person,self.start,self.end)

    def toJson(self):
        return {
            'type' : "meeting",
            'person' : self.person,
            'subject' : self.subject,
            'startTime': str(self.start),
            'endTime': str(self.end)
        }