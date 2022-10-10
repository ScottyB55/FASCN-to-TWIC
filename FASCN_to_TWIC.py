# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:19:23 2022

@author: srbur
"""

def string_to_clusters(str, cluster_length):
    """
    splits up a string starting with '0b' into clusters of length cluster_length

    Parameters
        str (string): a binary string starting with '0b'
        cluster_length (int): how long should each cluster be? (5)

    Returns
        chunks (list): a list of strings representing each binary cluster,
            each of length cluster_length
    """
    str = str[2:] # chop off the '0b'
    chunks = [str[i:i+cluster_length] for i in range(0, len(str), cluster_length)]
    return chunks

def cluster_5b_to_string(strb):
    """
    converts a cluster (5 bit binary string) into its corresponding value (string)

    Parameters
        strb (string) : a 5 bit binary string

    Returns
        A single character digit or a 2 character sentinel 
    """
    # chop off the parity bit and reverse for MSB first
    MSB_first_no_parity = strb[3::-1]
    # convert the binary string to a decimal
    decimal_value = int(MSB_first_no_parity, 2)
    # convert the cluster decimal into its corresponding string
    if decimal_value < 10:
        return str(decimal_value)
    if decimal_value == 11:
        return "SS"
    if decimal_value == 13:
        return "FS"
    if decimal_value == 15:
        return "ES"
    # no matches
    raise Exception("Invalid cluster conversion: " + str(decimal_value))

def fascn_to_twic(FASCN_hex_string):
    """
    converts a FASCN hex string into a TWIC string

    Parameters
        FASCN_hex_string (string) : a 50 character long hex string

    Returns
        A TWIC string
    """
    # Check for invalid FASCN length
    if (len(FASCN_hex_string) != 50):
        raise Exception("Invalid FASCN string length. Expected length is 50.")
        return
    
    # Convert the FASCN hex string to a binary string
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
            
        str_clusters.append(str_cluster)
    
    # Check for invalid FASCNs
    # This list is incomplete. It doesn't check for everything
    if (str_clusters[0] != "SS"):
        raise Exception("FASCN doesn't start with SS")
    if (str_clusters[38] != "ES"):
        raise Exception("FASCN doesn't end with ES")
    
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