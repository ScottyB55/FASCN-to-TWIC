# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:19:23 2022

@author: srbur
"""

# split up a string starting with '0b' into clusters of length cluster_length
# https://pythonexamples.org/python-split-string-into-specific-length-chunks/
def string_to_clusters(str, cluster_length):
    str = str[2:] # chop off the '0b'
    chunks = [str[i:i+cluster_length] for i in range(0, len(str), cluster_length)]
    return chunks

# convert a cluster (5 bit binary string) into its corresponding string
def cluster_5b_to_string(strb):
    # chop off the parity bit and reverse for MSB first
    # https://www.w3schools.com/python/python_howto_reverse_string.asp
    MSB_first_no_parity = strb[3::-1]
    # convert the binary string to a decimal
    # https://stackoverflow.com/questions/2072351/python-conversion-from-binary-string-to-hexadecimal
    decimal_value = int(MSB_first_no_parity, 2)
    # convert the cluster decimal into its corresponding string
    if decimal_value < 10:
        return str(decimal_value)
    elif decimal_value == 11:
        return "SS"
    elif decimal_value == 13:
        return "FS"
    elif decimal_value == 15:
        return "ES"
    else:
        raise Exception("Invalid cluster conversion: " + str(decimal_value))
        return

# convert a FASCN hex string into a TWIC string
def fascn_to_twic(FASCN_hex_string):
    # Check for invalid FASCN length
    if (len(FASCN_hex_string) != 50):
        raise Exception("Invalid FASCN string length. Expected length is 50.")
        return
    
    # Convert the FASCN hex string to a binary string
    # https://www.skillsugar.com/how-to-convert-hexadecimal-to-binary-in-python#:~:text=To%20convert%20hexadecimal%20to%20binary%20form%2C%20first%2C%20convert%20it%20to,get%20binary%20from%20the%20decimal.
    FASCN_binary_string = bin(int(FASCN_hex_string, 16))
    
    # split up the binary string into clusters of 5 bits
    # 4 bits for hex and 1 bit for parity
    FASCN_5_bit_clusters = string_to_clusters(FASCN_binary_string, 5)
    
    # go through the clusters and convert them into their corresponding string
    str_clusters = []
    for index, value in enumerate(FASCN_5_bit_clusters):
        try:
            str_cluster = cluster_5b_to_string(value)
        # pass on the exception from cluster_5b_to_string()
        except Exception as e:
            raise Exception("Cluster index " + index + ": " + str(e))
            return
            
        str_clusters.append(str_cluster)
    
    # Check for invalid FASCNs
    # This list is incomplete. It doesn't check for everything
    if (str_clusters[0] != "SS"):
        raise Exception("FASCN doesn't start with SS")
        return
    if (str_clusters[38] != "ES"):
        raise Exception("FASCN doesn't end with ES")
        return
    
    # Split the cluster strings up into desired codes
    agency_code = str_clusters[1:5]
    system_code = str_clusters[6:10]
    credential_number = str_clusters[11:17]
    
    # Reconstruct these codes as a TWIC String
    array_TWIC = agency_code + system_code + credential_number;
    str_TWIC = ""
    for string in array_TWIC:
        str_TWIC += string;
    
    return str_TWIC