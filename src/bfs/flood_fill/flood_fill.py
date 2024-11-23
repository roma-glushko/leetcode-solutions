from typing import List


class FloodFill:
    """
    Problem Link: https://leetcode.com/problems/flood-fill/
    Complexity: Easy
    """

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, new_color: int
    ) -> List[List[int]]:
        old_color = image[sr][sc]

        if old_color == new_color:
            return image

        img_height = len(image)
        img_width = len(image[0])

        current_pixels = [(sr, sc)]

        while current_pixels:
            next_pixels = []

            for sr, sc in current_pixels:
                image[sr][sc] = new_color

                if sr - 1 >= 0 and image[sr - 1][sc] == old_color:
                    # top nearest pixel
                    next_pixels.append((sr - 1, sc))

                if sr + 1 < img_height and image[sr + 1][sc] == old_color:
                    # bottom nearest pixel
                    next_pixels.append((sr + 1, sc))

                if sc - 1 >= 0 and image[sr][sc - 1] == old_color:
                    # left nearest pixel
                    next_pixels.append((sr, sc - 1))

                if sc + 1 < img_width and image[sr][sc + 1] == old_color:
                    # right nearest pixel
                    next_pixels.append((sr, sc + 1))

                current_pixels = next_pixels

        return image
