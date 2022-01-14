# Note: the class must be called Test

import unittest
from solution import sort_array


class Test(unittest.TestCase):
  def test_sort_array(self):
    unordered = [2, 4, 34, 6, 21, 18, 24, 29, 31, 18, 48, 40, 35, 19,  5,  4, 22, 32, 38, 23, 42, 43, 18, 2, 23, 9, 36, 21, 3, 16]
    ordered = [2, 2, 3, 4, 4, 5, 6, 9, 16, 18, 18, 18, 19, 21, 21, 22, 23, 23, 24, 29, 31, 32, 34, 35, 36, 38, 40, 42, 43, 48]
    self.assertEqual(sort_array(unordered), ordered) 
    
    unordered2 = [3,5,7,8,1]
    ordered2 = [1,3,5,7,8]
    self.assertEqual(sort_array(unordered2), ordered2)
    
    unordered3 = [780, 55, 53, 55, 2, 78]
    ordered3 = [2, 53, 55, 55, 78, 780]
    self.assertEqual(sort_array(unordered3), ordered3)
