
import logging
logger = logging.getLogger(__name__)


from .date import Date
from .freeslot import Freeslot

class Calendar(object):

    def __init__(self,backend):
        self.backend = backend


    def process(self,start:Date=None,end:Date=None):
        logger.info("[CALENDAR][PROCESS]Build calendar from %s to %s" % (start,end))
        """
            Seems the search logic as follows :            
            1. If we have any meeting in some day, find a empty slots same day.
            2. If we don't have any meetings, just skip the day
        """
        calendar_events = self.backend.events(start,end)
        event = next(calendar_events)

        if event is None:
            """ We don't have any meetings at all. Return empty list """
            return []

        logger.debug("[CALENDAR][PROCESS]First event start time %s" % event.start)
        start_date = start
        if start_date is None:
            start_date = event.start.day()
            logger.debug("[CALENDAR][PROCESS]Set start date to first event %s" % start_date)

        if start_date.days() < event.start.days(): 
            """ The case when  search date less then first meeting in our DB"""
            start_date = event.start.day()
            logger.debug("[CALENDAR][PROCESS]Start date changed %s" % start_date)

        if start_date < event.start:
            """ There is empty slot in the beginig of th date """
            yield Freeslot(start_date,event.start)

        for ev in calendar_events:
            """ Enumerate event and fill free slots """
            if event.end < ev.start:
                """ There is free slot """
                yield Freeslot(event.end,ev.start)
                event = ev
            if ev.end > event.end:
                """ Just append busy event slot """
                event += ev
            yield ev

            """ Freeslot till 23:59 """        
        yield Freeslot(event.end,event.end.night())

    def find(self,args):

        start_date = Date.fromDateString(args[0],True)
        end_date = Date.fromDateString(args[1],False)

        logger.info("[CALENDAR][FIND]Search free time from %s to %s" % (start_date,end_date))

        for ev in self.process(start_date,end_date):
            if ev.type == 'free':
                logger.debug("[CALENDAR][FIND]Found empty slot " + str(ev))
                yield ev 

    def show(self,args):

        start_date = Date.fromDateString(args[0],True)
        end_date = Date.fromDateString(args[1],False)
        
        return self.process(start_date,end_date)
