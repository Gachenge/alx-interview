#!/usr/bin/python3
"""
technical interview questions to improve my ability to problem solve
"""


def pascal_triangle(n):
    """makes a list of lists that represents pascals triangle"""
    if n <= 0:
        return []
    arr = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if (j < i):
                if j == 0:
                    arr[i].append(1)
                else:
                    arr[i].append(arr[i - 1][j] + arr[i - 1][j - 1])
            elif j == i:
                arr[i].append(1)
    return arr
