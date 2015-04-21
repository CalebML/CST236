"""
Test for source.ORC
"""
import logging
from source.orc import orc
from unittest import TestCase

class TestORC(TestCase):
    def setUp(self):
        self.obj = orc()
        self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)

    def test__init__nothing_passed(self):
        #orc = __init__()
        self.assertEqual(self.obj.name, 'Krusk')

    def test__init__all_passed(self):
        orc2 = orc(name='UG', locx=1000, locy=42, speed=2, orcType='Berserker', priority=5)
        self.assertEqual(orc2.name, 'UG')

    def test_name_length_long(self):
        orc2 = orc(name='This is a long name that should fail and default to Krusk')
        self.assertEqual(orc2.name, 'Krusk')

    def test_loc_boundery_x_small(self):
        orc2 = orc(locx=0)
        self.assertEqual(orc2.locx, 1)

    def test_loc_boundery_y_small(self):
        orc2 = orc(locy=0)
        self.assertEqual(orc2.locy, 1)

    def test_loc_boundery_x_big(self):
        orc2 = orc(locx=1001)
        self.assertEqual(orc2.locx, 1000)

    def test_loc_boundery_y_big(self):
        orc2 = orc(locy=1001)
        self.assertEqual(orc2.locy, 1000)

    def test_loc_robust(self):
        orc2 = orc(locx='five')
        self.assertEqual(orc2.locx, 1)

    def test_speed(self):
        orc2 = orc(speed=-1)
        self.assertEqual(orc2.speed, 0)

    def test_priority_low(self):
        orc2 = orc(priority=-1)
        self.assertEqual(orc2.priority, 0)

    def test_priority_high(self):
        orc2 = orc(priority=11)
        self.assertEqual(orc2.priority, 10)

    def test_orcType(self):
        orc2 = orc(orcType='General')
        self.assertEqual(orc2.orcType, 'General')

    def test_orcType_bad_val(self):
        orc2 = orc(orcType='BadVal')
        self.assertEqual(orc2.orcType, 'Scout')
