from typing import List, Set


class NumberOfIslands:
    """
    Problem Link: https://leetcode.com/problems/number-of-islands/
    Complexity: Medium
    """

    water_type: str = "0"
    land_type: str = "1"

    def get_land_id(self, row_idx: int, col_idx: int) -> str:
        return "{}:{}".format(row_idx, col_idx)

    def numIslands(self, grid: List[List[str]]) -> int:
        grid_height = len(grid)
        grid_width = len(grid[0])

        num_of_islands: int = 0
        explored_lands: Set = set()

        def explore_island(row_idx: int, col_idx: int) -> None:
            land_id: str = self.get_land_id(row_idx, col_idx)

            if land_id in explored_lands:
                return

            explored_lands.add(land_id)

            if row_idx - 1 >= 0 and grid[row_idx - 1][col_idx] == self.land_type:
                # top cell
                explore_island(row_idx - 1, col_idx)

            if (
                row_idx + 1 < grid_height
                and grid[row_idx + 1][col_idx] == self.land_type
            ):
                # bottom cell
                explore_island(row_idx + 1, col_idx)

            if col_idx - 1 >= 0 and grid[row_idx][col_idx - 1] == self.land_type:
                # left cell
                explore_island(row_idx, col_idx - 1)

            if (
                col_idx + 1 < grid_width
                and grid[row_idx][col_idx + 1] == self.land_type
            ):
                # right cell
                explore_island(row_idx, col_idx + 1)

        for row_idx, grid_row in enumerate(grid):
            for col_idx, cell_type in enumerate(grid_row):
                if cell_type == self.water_type:
                    # water cell, nothing to count here
                    continue

                # found a land cell
                land_id: str = self.get_land_id(row_idx, col_idx)

                if land_id in explored_lands:
                    # we have been there before, go ahead to the next cell
                    continue

                # we found an unseen land cell
                num_of_islands += 1
                explore_island(row_idx, col_idx)

        return num_of_islands
