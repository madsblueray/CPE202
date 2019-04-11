import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
    
    def test_max_list_iter1(self):
        tlist = [1,2,3,4,5,6,7,8]
        self.assertEqual(max_list_iter(tlist), 8)
    
    def test_max_list_iter2(self):
        tlist = [8,7,6,5,4,3,2,1]
        self.assertEqual(max_list_iter(tlist), 8)

    def test_max_list_iter3(self):
        tlist = [8,8,8,8,8,8,8,8]
        self.assertEqual(max_list_iter(tlist), 8)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec1(self):
        self.assertEqual(reverse_rec([1,2,3,4]),[4,3,2,1])

    def test_reverse_rec2(self):
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4 )

    def test_bin_search1(self):
        list_val =[0,2,4,8,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(10, low, high, list_val), 4 )

    def test_bin_search2(self): #checks that a midpoint is being correctly established
        list_val =[2,2,2,2,2]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(2, low, high, list_val), 2 )

    def test_bin_search3(self):
        list_val =[0,2,4,8,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(3, low, high, list_val), None )

    def test_bin_search4(self):
        list_val =[]
        low = 0
        high = len(list_val)-1
        with self.assertRaises(ValueError):
            bin_search(4, low, high, list_val)

if __name__ == "__main__":
        unittest.main()

