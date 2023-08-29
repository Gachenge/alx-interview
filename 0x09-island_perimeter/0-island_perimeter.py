#!/usr/bin/python3

def island_perimeter(grid):
    if not grid:
        return 0
    M, N = len(grid), len(grid[0])
    perim = 0

    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perim += 1
                if j == 0 or grid[i][j-1] == 0:
                    perim += 1
                if i == M-1 or grid[i+1][j] == 0:
                    perim += 1
                if j == N-1 or grid[i][j+1] == 0:
                    perim += 1

    return perim
