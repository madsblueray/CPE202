import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_repr1(self):
        loc = Location("LA", 30.3, -2.7)
        self.assertEqual(repr(loc),"Location('SLO', 30.3, -2.7)")

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc == loc1))

    def test_eq1(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("SLOWWWWWWW", 35.3, -120.7)
        self.assertFalse(loc == loc1))

    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
