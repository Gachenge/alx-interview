#!/usr/bin/python3
"""
script to determine if a dataset is valid utf-8 encoding
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
"""


def validUTF8(data):
    """determine if the data is valid encoded"""
    try:
        data = bytes(data)
        dec = data.decode('utf-8')
        return True
    except Exception as e:
        return False
