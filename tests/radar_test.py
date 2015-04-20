"""
Test for source.radar
"""
import logging
from source.orc import orc
from source.radar import radar
from unittest import TestCase

class TestORC(TestCase):
    def setUp(self):
        #self.orc = orc()
        self.obj = radar()
        self.orc = orc()
        self.obj.addOrc(orc)
        self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)

    def test__init__(self):
        self.assertEqual(self.obj.maxOrcs, 25)

    def test_add_orc(self):
        orc2 = orc(name='UG')
        self.obj.addOrc(orc2)
        self.assertEqual(self.obj.numOrcs, 2)

    def test_quit(self):
        self.obj.command('X')
        self.assertFalse(hasattr(self.obj, 'maxOrcs'))

    def test_distance(self):
        distance = self.obj.distance('Krusk')
        self.assertEqual(distance, 998)

    def test_speed(self):
        speed = self.obj.speed('Krusk')
        self.assertEqual(speed, 1)
        
