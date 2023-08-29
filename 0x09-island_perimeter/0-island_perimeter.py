#!/usr/bin/python3

"""each side of the square is 1 unit long"""

def island_perimeter(grid):
    """
    get the perimeter of an island. assume there are no holes
    """
    if not grid:
        return 0
    row, col = len(grid), len(grid[0])
    perim = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perim += 1
                if j == 0 or grid[i][j-1] == 0:
                    perim += 1
                if i == row-1 or grid[i+1][j] == 0:
                    perim += 1
                if j == col-1 or grid[i][j+1] == 0:
                    perim += 1

    return perim
