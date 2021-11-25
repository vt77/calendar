
import json

import logging
logger = logging.getLogger(__name__)

json_data = []

def open(action:str):
    json_data = []

def out(data:list):
    for p in data:
        logger.debug("[OUTPUT][JSON]Add timeslot %s", json.dumps(p.toJson()))
        json_data.append( p.toJson() )

def close():
    logger.debug("[OUTPUT][JSON]Added  %d timeslots" % len(json_data))
    print( json.dumps(json_data,indent=4) )