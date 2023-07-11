#!/usr/bin/python3
"""find minimum copy paste operations"""


def minOperations(n):
    """result in exactly n characters"""
    if (n <= 1):
        return 0
    else:
        for i in range(2, int((n/2) + 1)):
            if n % i == 0:
                return minOperations(int(n / i)) + i
    return n
