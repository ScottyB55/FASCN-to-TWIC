# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:50:54 2022

@author: srbur
"""

import unittest
from FASCN_to_TWIC import fascn_to_twic

class FASCN_Unit_Test(unittest.TestCase):
    # Tests Provided from PSI
    def test1(self):
        input_string = "D70339DA15256C10843C45A16858210D5B3CCC90870339A3FF"
        output_string = "70991545000072"
        assert fascn_to_twic(input_string) == output_string
        
    def test2(self):
        input_string = "D70339DAA108AC120790CDA16858210D5B3CCC90870339A3F9"
        output_string = "70995008040713"
        assert fascn_to_twic(input_string) == output_string
        
    def test3(self):
        input_string = "D70339DAA108AC18343C45A16458210C262986A2870339A3E8"
        output_string = "70995008016072"
        assert fascn_to_twic(input_string) == output_string
    
    # Check for invalid FASCN string length
    def test_string_length(self):
        input_string = "70339DA15256C10843C45A16858210D5B3CCC90870339A3FF"
        self.assertRaises(Exception, fascn_to_twic(input_string))
    
    # Check for FASCN not starting with SS
    def test_ss_start(self):
        input_string = "A70339DA15256C10843C45A16858210D5B3CCC90870339A3FF"
        self.assertRaises(Exception, fascn_to_twic(input_string))
        
    # Check for FASCN not ending with ES
    def test_es_end(self):
        input_string = "D70339DA15256C10843C45A16858210D5B3CCC90870339A3AA"
        self.assertRaises(Exception, fascn_to_twic(input_string))

test = FASCN_Unit_Test()
test.test1()
test.test2()
test.test3()
# test.test_string_length()

print("Tests Passed.")

# can test a couple edge cases, like when it is empty
# show that the function is robust

# https://www.youtube.com/watch?v=LxbiAHGkPhk
# https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception