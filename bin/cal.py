#!/usr/bin/python3 

import os,sys,time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib')))


#User defined timezone
os.environ['TZ'] = 'UTC'
time.tzset()

import traceback
import logging
#TODO: Make logger configuration
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()

if len(sys.argv) == 1:
    print("Usage : %s <action> [action parameters]" % sys.argv[0])
    exit(1)


"""
Load our application modules 
"""
from backend import jsonfile as backend
from zigicalendar import calendar
#import output.consoleprinter as printer
import output.jsonprinter as printer
import argparser

try :

    arg = argparser.parse(sys.argv[1:])
    calendar = calendar(backend(arg.datafile))

    '''
       Action input string is untrusted, don't call class explictly,
       validate allowed methods  
    '''
    calendar_actions = {
        'find' : calendar.find ,
        'show' : calendar.show
    }

    if arg.action not in calendar_actions:
        raise Exception("Unknown command " + arg.action)

    result =  calendar_actions[arg.action](arg.params)

except Exception as e :
    logger.error(str(e) + " " + traceback.format_exc() )
    exit(1)

printer.open(arg.action)
printer.out(result)
printer.close()
