

from datetime import datetime
from datetime import timezone
import time

class Date(object):
    '''
        Date class for zigi calendar
    '''
    def __init__(self,time:int,timezone='IL'):
        self._minutes = int(time / 60)
        self._timeZone = timezone

    @staticmethod
    def fromISO8601(datestring:str):
        '''
            Creates Date object from ISO8601 string
        '''
        #WARNING ! fromisoformat requires python >= 3.7
        date = datetime.fromisoformat(datestring)
        return Date(date.timestamp(),date.tzinfo)

    @staticmethod
    def fromDateString(datestring:str, start:bool):
        """
            Creates Date object from string in format : 2021-03-08
        """
        datetime_string  = "%s %s" % ( datestring, '00:00' if start else '23:59')
        date = datetime.strptime(datetime_string, '%Y-%m-%d %H:%M')
        return Date(date.timestamp(),date.tzinfo)


    def minutes(self):
        """ Returns unixtime in minutes """
        return self._minutes

    def timezone(self):
        """ Returns timezone """
        return self._timeZone

    def days(self):
        """ Returns unixtime in days """
        return int(self._minutes / 1440)

    def day(self):
        """ Returns start of day Date object"""
        return Date( int(self._minutes / 1440) * 1440 * 60, self._timeZone)

    def night(self):
        """ Returns start of day Date object"""
        return Date( (int(self._minutes / 1440) * 1440 + 1439)* 60, self._timeZone)

    def __repr__(self):
        # Uncomment this for debug
        #str(self._minutes) 
        
        # This is short local time with timezone 
        #return time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime( self._minutes * 60 ) )
        
        #ISO8601 in UTC
        #return datetime.fromtimestamp( self._minutes * 60 ).replace(tzinfo=timezone.utc).isoformat()
        
        #ISO8601 in localtime include timezone
        return datetime.fromtimestamp( self._minutes * 60 ).astimezone().isoformat()

    def __cmp__(self,other):
        if self._minutes == other.minutes():
                return 0
        return 1 if self._minutes >  other.minutes() else -1 
    
    def __lt__(self,other):
        return self._minutes <  other.minutes()