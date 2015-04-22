"""
Test for source.radar
"""
import logging
from source.orc import orc
from source.radar import radar
from unittest import TestCase

class TestRadar(TestCase):
    def setUp(self):
        self.obj = radar()
        testOrc = orc()
        self.obj.addOrc(testOrc)
        self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)

    def test__init__(self):
        self.assertEqual(self.obj.numOrcs, 1)

    def test_add_orc(self):
        orc2 = orc(name='UG')
        self.obj.addOrc(orc2)
        self.assertEqual(self.obj.numOrcs, 2)

    def test_add_orc_same_name(self):
        orc2 = orc(name='Krusk')
        self.obj.addOrc(orc2)
        self.assertEqual(self.obj.numOrcs, 1)

    def test_quit(self):
        self.obj.command('X')
        self.assertFalse(hasattr(self.obj, 'numOrcs'))

    def test_distance(self):
        distance = self.obj.distance('Krusk')
        self.assertEqual(distance, 998)

    def test_speed(self):
        speed = self.obj.speed('Krusk')
        self.assertEqual(speed, 1)
        
    def test_help(self):
        retVal = self.obj.command('?')
        self.assertEqual(retVal, """? - pull up this message
                         X - Quit
                         u - shows or sets units
                            ex. 'U, meters'
                         l - list orcs on battlefield
                             ex. L, Scout""")

    def test_remove_last_orc(self):
        self.obj.killOrc('Krusk')
        self.assertEqual(self.obj.numOrcs, 0)

    def test_remove_orc(self):
        orc2 = orc(name='UG')
        self.obj.addOrc(orc2)
        self.obj.killOrc('Krusk')
        self.assertEqual(self.obj.numOrcs, 1)

    def test_check_units(self):
        retVal = self.obj.command('u')
        self.assertEqual(retVal, 'yards')

    def test_change_units_PASS(self):
        retVal = self.obj.command('u', 'meters')
        self.assertEqual(retVal, 'meters')

    def test_change_units_FAIL(self):
        self.obj.command('u', 'meters')
        self.obj.command('u', 'BadVal')
        retVal = self.obj.command('u')
        self.assertEqual(retVal, 'meters')

    def test_list_orcs(self):
        retVal = self.obj.command('l')
        self.assertEqual(retVal[0].name, 'Krusk')
        
    def test_empty_list_orcs(self):
        self.obj.killOrc('Krusk')
        retVal = self.obj.command('l')
        self.assertEqual(len(retVal), 0)

    def test_set_priority(self):
        retVal = self.obj.setPriority('Krusk', 5)
        self.assertEqual(retVal, 5)

    def test_set_priority_high(self):
        retVal = self.obj.setPriority('Krusk', 50)
        self.assertEqual(retVal, 10)
        
    def test_list_orcs_by_type(self):
        orc2 = orc(name='UG', orcType='Scout')
        self.obj.addOrc(orc2)
        orc3 = orc(name='Urag', orcType='War Chief')
        self.obj.addOrc(orc3)
        orc4 = orc(name='Orbkh', orcType='General')
        self.obj.addOrc(orc4)
        retVal = self.obj.command('l', 'Scout')
        self.assertEqual(len(retVal), 2)
        
    def test_list_orcs_by_type_empty(self):
        retVal = self.obj.command('l', 'General')
        self.assertEqual(len(retVal), 0)

    def test_look_at_1_orc(self):
        retVal = self.obj.command('l', 'Krusk')
        self.assertEqual(retVal.name, 'Krusk')

    def test_look_at_1_orc_not_found(self):
        self.obj.killOrc('Krusk')
        retVal = self.obj.command('l', 'Krusk')
        self.assertEqual(retVal, None)
    
    def test_ENTer_the_trees(self):
        orc2 = orc(name='UG', orcType='Scout')
        self.obj.addOrc(orc2)
        orc3 = orc(name='Urag', orcType='War Chief')
        self.obj.addOrc(orc3)
        orc4 = orc(name='Orbkh', orcType='General')
        self.obj.addOrc(orc4)
        self.obj.command('ENTer the trees')
        retVal = self.obj.command('l')
        self.assertEqual(len(retVal), 0)

    def test_generate_orcs(self):
        self.obj.genOrcs()
        self.obj.genOrcs()
        self.obj.genOrcs()
        retVal = self.obj.command('l')
        self.assertEqual(len(retVal), 4)
        



        

