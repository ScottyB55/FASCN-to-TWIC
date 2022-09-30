# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:50:54 2022

@author: srbur
"""

from FASCN_to_TWIC import fascn_to_twic, b5_to_string

def test1():
    input_string = "D70339DA15256C10843C45A16858210D5B3CCC90870339A3FF"
    output_string = "70991545000072"
    assert fascn_to_twic(input_string) == output_string
    
def test2():
    input_string = "D70339DA15256C10843C45A16858210D5B3CCC90870339A3FF"
    output_string = "70991545000072"
    assert fascn_to_twic(input_string) == output_string
    
def test3():
    input_string = "F70339DA15256C10843C45A16858210D5B3CCC90870339A3FF"
    output_string = "70991545000072"
    b5_to_string("01111");
    assert fascn_to_twic(input_string) == output_string

# can test a couple edge cases, like when it is empty
# show that the function is robust
test1()
test2()
test3()