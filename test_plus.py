#!/usr/bin/env python

import unittest
from plus import plus

'''
    test env: for Function "plus()@plus.py"
'''

#---------------
class TestPlus(unittest.TestCase):

    def test_int(self):
        self.assertEqual(plus(1,2), 3, "error on int")

    def test_float(self):
        self.assertTrue(3.299<plus(1.1,2.2)<3.3301, "error on float")
     
    def test_str(self):
        self.assertEqual(plus("ab","cd"), "abcd", "error on str")
#---------------


##############################
#
#
#
##############################
unittest.main()