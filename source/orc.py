"""
:mod:`source.orc` -- source code for an orc object
============================================

"""

import logging

logger = logging.getLogger(__name__)
orcTypeList = ['Scout', 'Grunt', 'Raider', 'Berserker', 'Band Master', 'Captain', 'General', 'War Chief']

class orc(object):  #Orc class
    def __init__(self, name='Krusk', locx=1, locy=1, speed=1, orcType='Scout', priority=1):
        #set name
        if(len(name) < 20):
            self.name = name
        else:
            self.name = 'Krusk'
            logger.warning('Default name used')
            
        #set x coord
        if(isinstance(locx, int) != True):
            self.locx = 1
            logger.warning('x coordinate set to 1, Not an int')
        elif(locx < 1):
            self.locx = 1
            logger.warning('x coordinate set to 1, passed value to low')
        elif(locx > 1000):
            self.locx = 1000
            logger.warning('x coordinate set to 1000, passed value to high')
        else:
            self.locx = locx
            
        #set y coord
        if(isinstance(locy, int) != True):
            self.locy = 1
            logger.warning('y coordinate set to 1, Not an int')
        elif(locy < 1):
            self.locy = 1
            logger.warning('y coordinate set to 1, passed value to low')
        elif(locy > 1000):
            self.locy = 1000
            logger.warning('y coordinate set to 1000, passed value to high')
        else:
            self.locy = locy

        #set speed
        if(speed < 0):
            self.speed = 0
            logger.warning('speed set to 0, passed value cannot be negative')
        else:
            self.speed = speed

        #set rank
        if(orcType in orcTypeList):
            self.orcType = orcType
        else:
            self.orcType = 'Scout'

        #set Priority
        if(isinstance(priority, int) != True):
            self.priority = 1
            logger.warning('Priority set to 1, Not an int')
        elif(priority < 0):
            self.priority = 0
            logger.warning('Priority set to 1, passed value to low')
        elif(priority > 10):
            self.priority = 10
            logger.warning('Priority set to 10, passed value to high')
        else:
            self.priority = priority

        logger.info('Orc created!')



