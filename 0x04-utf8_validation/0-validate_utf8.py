#!/usr/bin/python3
"""script to determine if a dataset is valid utf-8 encoding"""


def validUTF8(data):
    """determine if the data is valid encoded"""
    try:
        data = bytes(data)
        dec = data.decode('utf-8')
        return True
    except Exception as e:
        return False
