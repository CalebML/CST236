"""
Radar
"""

import logging
from source.orc import orc
from source.orc import orcTypeList

logger = logging.getLogger(__name__)

unitList = ['yards', 'meters', 'parsecs']

class radar(object):
    """
    radar Class
    """
    def __init__(self, units='yards'):
        self.numOrcs = 0
        self.orcList = []
        self.units = 'yards'
        logger.info('Radar created!')

    def addOrc(self, Orc):
        error = False
        for orc in self.orcList:
            if Orc.name in orc.name:
                logger.error('Orcs must have a unique name')
                error = True
                break
        if(error == False):
            self.numOrcs = self.numOrcs +1
            self.orcList.append(Orc)
            logger.info('Orc added to battlefield!')

    def killOrc(self, name):
        for orc in self.orcList:
            if name in orc.name:
                self.orcList.remove(orc)
                self.numOrcs = self.numOrcs -1
                break

    def distance(self, name):
        retVal = None
        logger.debug('calculating distance')
        for orc in self.orcList:
            if name in orc.name:
                retVal = ( (500 - orc.locx) + (500 - orc.locy) )
                break
        return retVal

    def speed(self, name):
        retVal = None
        for orc in self.orcList:
            if name in orc.name:
                retVal = orc.speed
                break
        return retVal

    def setPriority(self, name, priority):
        retVal = None
        for orc in self.orcList:
            if name in orc.name:
                if(isinstance(priority, int) != True):
                    orc.priority = 1
                    logger.warning('Priority set to 1, Not an int')
                elif(priority < 0):
                    orc.priority = 0
                    logger.warning('Priority set to 1, passed value to low')
                elif(priority > 10):
                    orc.priority = 10
                    logger.warning('Priority set to 10, passed value to high')
                else:
                    orc.priority = priority
                retVal = orc.priority
                break
        return retVal

    def command(self, command='?', val=None):
        retVal = None
        if (command == 'x') or (command == 'X'):
            del self.numOrcs
            del self.orcList
            del self
            
        elif (command == 'u') or (command == 'U'):
            if (val == None):
                retVal = self.units
            elif (val in unitList):
                self.units = val
                retVal = val

        elif (command == 'l') or (command == 'L'):
            if (val == None):
                retVal = self.orcList
            elif (val in orcTypeList):
                retList = []
                for orc in self.orcList:
                    if orc.orcType == val:
                        retList.append(orc)
                retVal = retList;
        
        elif (command == '?'):
            retVal = """? - pull up this message
                         X - Quit
                         u - shows or sets units
                            ex. 'U, meters'
                         l - list orcs on battlefield
                             ex. L, Scout"""
        return retVal
