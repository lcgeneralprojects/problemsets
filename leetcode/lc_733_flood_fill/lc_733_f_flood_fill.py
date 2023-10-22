from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        to_fill = [[sr, sc]]
        area_color = image[sr][sc]

        if area_color == color:
            return image

        while to_fill:
            pixel = to_fill.pop(0)

            image[pixel[0]][pixel[1]] = color

            if pixel[0] - 1 in range(len(image)) and pixel[1] in range(len(image[0])) and image[pixel[0] - 1][
                pixel[1]] == area_color:
                to_fill.append([pixel[0] - 1, pixel[1]])
            if pixel[0] in range(len(image)) and pixel[1] - 1 in range(len(image[0])) and image[pixel[0]][
                pixel[1] - 1] == area_color:
                to_fill.append([pixel[0], pixel[1] - 1])
            if pixel[0] + 1 in range(len(image)) and pixel[1] in range(len(image[0])) and image[pixel[0] + 1][
                pixel[1]] == area_color:
                to_fill.append([pixel[0] + 1, pixel[1]])
            if pixel[0] in range(len(image)) and pixel[1] + 1 in range(len(image[0])) and image[pixel[0]][
                pixel[1] + 1] == area_color:
                to_fill.append([pixel[0], pixel[1] + 1])

        return image
