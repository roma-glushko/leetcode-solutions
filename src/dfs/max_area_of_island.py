from typing import List, Set


class MaxAreaOfIsland:
    """
    Problem Link: https://leetcode.com/problems/max-area-of-island/
    """

    water_type: int = 0
    land_type: int = 1

    def get_land_id(self, row_idx: int, col_idx: int) -> str:
        return "{}:{}".format(row_idx, col_idx)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        grid_height = len(grid)
        grid_width = len(grid[0])

        max_area: int = 0
        explored_lands: Set = set()

        def calculate_island_area(row_idx: int, col_idx: int) -> int:
            land_id = self.get_land_id(row_idx, col_idx)

            if land_id in explored_lands:
                return 0

            explored_lands.add(land_id)

            island_area = 1

            if row_idx - 1 >= 0 and grid[row_idx - 1][col_idx] == self.land_type:
                # top cell
                island_area += calculate_island_area(row_idx - 1, col_idx)

            if row_idx + 1 < grid_height and grid[row_idx + 1][col_idx] == self.land_type:
                # bottom cell
                island_area += calculate_island_area(row_idx + 1, col_idx)

            if col_idx - 1 >= 0 and grid[row_idx][col_idx - 1] == self.land_type:
                # left cell
                island_area += calculate_island_area(row_idx, col_idx - 1)

            if col_idx + 1 < grid_width and grid[row_idx][col_idx + 1] == self.land_type:
                # right cell
                island_area += calculate_island_area(row_idx, col_idx + 1)

            return island_area

        for row_idx, grid_row in enumerate(grid):
            for col_idx, cell_type in enumerate(grid_row):
                if cell_type == self.water_type:
                    # it's a water cell. Nothing to do here
                    continue

                land_id = self.get_land_id(row_idx, col_idx)

                if land_id in explored_lands:
                    # the land cell is already explored. Go to the next one
                    continue

                # we found an unseen land, let's explore it!

                island_area = calculate_island_area(row_idx, col_idx)

                if island_area > max_area:
                    max_area = island_area

        return max_area
