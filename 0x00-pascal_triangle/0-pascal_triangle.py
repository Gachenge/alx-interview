#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    arr = [[] for i in range (n)]
    for i in range(n):
        for j in range(i + 1):
            if (j < i):
                if j == 0:
                    arr[i].append(1)
                else:
                    arr[i].append(arr[i-1][j] +  arr[i -1][j-1])
            elif j == i:
                arr[i].append(1)
    return arr

