#!/usr/bin/python3
"""
script to determine if a dataset is valid utf-8 encoding
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
"""
import codecs


def validUTF8(data):
    """determine if the data is valid encoded"""
    try:
        byte_data = bytes(data)
        codecs.utf_8_decode(byte_data)
        return True
    except Exception as e:
        return False
