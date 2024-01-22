""" sample test """

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """ Test The Calc Module """
    
    def test_add_number(self):
        """"Test adding the number together"""
        
        res = calc.add(5,6)
        
        self.assertEqual(res, 11)
        
        
    def test_substract_number(self):
        """Test substracting number"""
        
        res = calc.substract(10,15)
        
        self.assertEqual(res, 5)