

import sys
import json

import logging
logger = logging.getLogger(__name__)


from zigicalendar.meeting import Meeting
from zigicalendar.date import Date



class JsonFileBackend():

    """ File fields names constants """
    FIELD_NAME_PERSON      = "name"
    FIELD_NAME_SUBJECT      = "subject"
    FIELD_NAME_MEETINGS     = "meetings"
    FIELD_NAME_STARTTIME    = "startTime"
    FIELD_NAME_ENDTTIME    = "endTime"


    def __init__(self,datafile:str):
        #NOTE ! Contract style design says we always return values, even empty
        self.events_list = []
        #WARNING!  datafile variable is untrusted. Should be validated.
        logger.info("[BACKEND][JSON]Loading file " + datafile)
        with open('data/' + datafile ) as f:
            json_data = json.load(f)
            for calendar in json_data:
                self.events_list.extend([ 
                                    Meeting( calendar[self.FIELD_NAME_PERSON],
                                            m[self.FIELD_NAME_SUBJECT],
                                            Date.fromISO8601(m[self.FIELD_NAME_STARTTIME]),
                                            Date.fromISO8601(m[self.FIELD_NAME_ENDTTIME])
                                    ) for m in  calendar[self.FIELD_NAME_MEETINGS]
                        ])
        self.events_list.sort()
        logger.info("[BACKEND][JSON]Loaded " + str(len(self.events_list)) + ' events' )

    def events(self,start_date=None):
        for event in self.events_list:
            yield event 

sys.modules[__name__] =  JsonFileBackend