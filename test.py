# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:50:54 2022

@author: srbur
"""

import unittest
from FASCN_to_TWIC import fascn_to_twic

class FASCN_Unit_Test(unittest.TestCase):
    def test1(self):
        """
        First test from PSI
        """
        input_string = "D70339DA15256C10843C45A16858210D5B3CCC90870339A3FF"
        output_string = "70991545000072"
        assert fascn_to_twic(input_string) == output_string
        
    def test2(self):
        """
        Second test from PSI
        """
        input_string = "D70339DAA108AC120790CDA16858210D5B3CCC90870339A3F9"
        output_string = "70995008040713"
        assert fascn_to_twic(input_string) == output_string
        
    def test3(self):
        """
        Third test from PSI
        """
        input_string = "D70339DAA108AC18343C45A16458210C262986A2870339A3E8"
        output_string = "70995008016072"
        assert fascn_to_twic(input_string) == output_string
    
    def test_string_length(self):
        """
        Check invalid FASCN string length exception
        """
        input_string = "70339DA15256C10843C45A16858210D5B3CCC90870339A3FF"
        with self.assertRaises(Exception):
            fascn_to_twic(input_string)
    
    def test_ss_start(self):
        """
        Check FASCN not starting with SS exception
        """
        input_string = "A70339DA15256C10843C45A16858210D5B3CCC90870339A3FF"
        with self.assertRaises(Exception):
            fascn_to_twic(input_string)
        
    def test_es_end(self):
        """
        Check FASCN not ending with ES exception
        """
        input_string = "D70339DA15256C10843C45A16858210D5B3CCC90870339A3AA"
        with self.assertRaises(Exception):
            fascn_to_twic(input_string)

"""
Run all the tests
"""
if __name__ == '__main__':
    unittest.main()

# can test a couple edge cases, like when it is empty
# show that the function is robust