from typing import List


class Solution:
    """
    Link: https://leetcode.com/problems/island-perimeter/
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        water = 0
        perimeter = 0

        for i, grid_columns in enumerate(grid):
            for j, grid_cell in enumerate(grid_columns):
                if grid_cell == water:
                    continue

                # calculate land cell perimeter

                if i - 1 < 0 or grid[i - 1][j] == water:
                    # top cell
                    perimeter += 1

                if i + 1 == height or grid[i + 1][j] == water:
                    # bottom cell
                    perimeter += 1

                if j - 1 < 0 or grid[i][j - 1] == water:
                    # left cell
                    perimeter += 1

                if j + 1 == width or grid[i][j + 1] == water:
                    # right cell
                    perimeter += 1

        return perimeter
