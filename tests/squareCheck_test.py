############################################
#squareCheck_test.py
#
#Takes: Nothing
#Returns:   Pass if all test succeed
#           Fail if any test fails
#
#Uses:  squareCheck.py
#       unittest.py
#
#Modified from source1_test.py
#
#Caleb Larson
#4/2/15
#CST 236
#
############################################
from source.squareCheck import get_rectangle_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

    def test_get_rectangle_rectangle_all_int(self):
        result = get_rectangle_type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    def test_get_rectangle_square_all_int(self):
        result = get_rectangle_type(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    def test_get_rectangle_invalid_all_int(self):
        result = get_rectangle_type(1, 2, 2, 1)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_invalid_tuple(self):
        result = get_rectangle_type( (1, 1, 2, 2) )
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_invalid_arg_type(self):
        result = get_rectangle_type(1, 2, 'One', 2)
        self.assertEqual(result, 'invalid')
        
    def test_get_rectangle_invalid_zero_int(self):
        result = get_rectangle_type(1, 0, 1, 0)
        self.assertEqual(result, 'invalid')

    def test_get_rectangle_dict(self):
        result = get_rectangle_type({'sideOne':1, 'sideTwo':2, 'sideThree':3, 'sideFour':4})
        self.assertEqual(result, 'invalid')
