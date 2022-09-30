# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:19:23 2022

@author: srbur
"""

import binascii

"""
Function Definitions
"""
# split up a binary string starting with '0b' into chunks
# returns a list
# https://pythonexamples.org/python-split-string-into-specific-length-chunks/
def string_to_chunks(str, chunk_length):
    str = str[2:] # chop off the '0b'
    chunks = [str[i:i+chunk_length] for i in range(0, len(str), chunk_length)]
    return chunks

def b5_to_string(strb):
    # chop off the parity bit and reverse for MSB first
    # https://www.w3schools.com/python/python_howto_reverse_string.asp
    MSB_first_no_parity = strb[3::-1]
    # convert the string to a decimal
    # https://stackoverflow.com/questions/2072351/python-conversion-from-binary-string-to-hexadecimal
    decimal_value = int(MSB_first_no_parity, 2)
    # convert the decimal to the real thing
    if decimal_value < 10:
        return str(decimal_value)
    elif decimal_value == 11:
        return "SS"
    elif decimal_value == 13:
        return "FS"
    elif decimal_value == 15:
        return "ES"
    else:
        raise Exception("Invalid hex. Must be mapped to a value")
        return

def fascn_to_twic(FASCN_hex_string):
    # Convert the hex string to a binary string
    # https://www.skillsugar.com/how-to-convert-hexadecimal-to-binary-in-python#:~:text=To%20convert%20hexadecimal%20to%20binary%20form%2C%20first%2C%20convert%20it%20to,get%20binary%20from%20the%20decimal.
    FASCN_binary_string = bin(int(FASCN_hex_string, 16))
    
    # split up the binary string into groups of 5 
    # this is for 4 bits of hex and 1 bit of parity
    FASCN_group_5_bits = string_to_chunks(FASCN_binary_string, 5)
    
    strings = []
    for index, value in enumerate(FASCN_group_5_bits):
        try:
            str_parse = b5_to_string(value)
        except Exception:
            raise Exception("Invalid input")
            return
        
        if ((index == 0) & (str_parse != "SS")):
            raise Exception("Doesn't start with SS")
            
        strings.append(str_parse)
    
    agency_code = strings[1:5]
    system_code = strings[6:10]
    credential_number = strings[11:17]
    
    arrTWIC = agency_code + system_code + credential_number;
    strTWIC = ""
    for string in arrTWIC:
        strTWIC += string;
    
    return strTWIC