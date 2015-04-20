"""
Radar
"""

import logging
from source.orc import orc

logger = logging.getLogger(__name__)

class radar(object):
    """
    radar Class
    """
    def __init__(self, maxOrcs=25):
        self.maxOrcs = maxOrcs
        self.numOrcs = 0
        self.orcList = [orc()]
        #del self.orcList[0]
        logger.info('Radar created!')

    def addOrc(self, Orc):
        self.numOrcs = self.numOrcs +1
        self.orcList.append(Orc)
        logger.info('Orc added to battlefield!')

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

    def command(self, command):
        retVal = None
        if (command == 'x') or (command == 'X'):
            del self.maxOrcs
            del self.numOrcs
            del self.orcList
            del self
        return retVal
