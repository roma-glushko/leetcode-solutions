from typing import List


class PascalsTriangle:
    """
    Problem Link: https://leetcode.com/problems/pascals-triangle/
    Complexity: Easy
    """
    def generate(self, num_rows: int) -> List[List[int]]:
        pascal_triangle: List[List[int]] = [[1]]

        for row_idx in range(num_rows):
            if row_idx == 0:
                continue

            next_triangle_row: List[int] = []

            previous_triangle_row: List[int] = pascal_triangle[row_idx - 1]
            previous_triangle_row_len: int = len(previous_triangle_row)

            for num_idx in range(previous_triangle_row_len + 1):
                # calculate the next triangle row
                left_parent_num: int = previous_triangle_row[num_idx - 1] if num_idx - 1 >= 0 else 0
                right_parent_num: int = previous_triangle_row[num_idx] if num_idx < previous_triangle_row_len else 0

                next_triangle_row.append(left_parent_num + right_parent_num)

            pascal_triangle.append(next_triangle_row)

        return pascal_triangle