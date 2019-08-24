import math
import os
from typing import List


class Image:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.pixels = list()
        # Default background is black
        self.start(0, 0, 0)

    def start(self, r: int, g: int, b: int) -> None:
        for row in range(self.rows):
            self.pixels.append([])
            for col in range(self.cols):
                self.pixels[row].append(f"{r} {g} {b}\n")

    def point(self, r: int, g: int, b: int, x: int, y: int) -> None:
        """
        point: we're drawing a single point
        ... 0 0 255: with this RGB color (blue)
        ... 0 0: at this coordinate (top left)
        """
        self.pixels[x][y] = f"{r} {g} {b}\n"

    @staticmethod
    def euclidean_distance(x1: int, y1: int, x2: int, y2: int):
        return math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))

    def line(self, r: int, g: int, b: int, x1: int, y1: int, x2: int, y2: int) -> None:
        """Given two points draw a line between them."""
        dx = x2 - x1
        dy = y2 - y1
        distance = int(round(
            math.sqrt((math.pow(dx, 2) + math.pow(dy, 2)))
        ))
        for i in range(distance):
            new_x = x1 + int(round((i / distance) * dx))
            new_y = y1 + int(round((i / distance) * dy))
            self.point(r, g, b, new_x, new_y)

    def bline(self, r: int, g: int, b: int, x0: int, y0: int, x1: int, y1: int) -> None:
        """
        Bresenham's line algorithm.

        Literally taken from here:
            https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
        """
        dx = abs(x1-x0)
        sx = 1 if x0 < x1 else -1

        dy = -abs(y1-y0)
        sy = 1 if y0 < y1 else -1

        err = dx+dy
        while True:
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx

            if e2 <= dx:
                err += dx
                y0 += sy

            self.point(r, g, b, x0, y0)

    def rect(self, r: int, g: int, b: int, x1: int, y1: int, x2: int, y2: int) -> None:
        """
        Drawing a rectangle
        r, g, b - RGB color
        x1, y1 - with its top left coordinate here.
        x2, y2 - with its sides being n pixels tall and n pixels wide
        """
        for row in range(x2):
            for col in range(y2):
                self.point(r, g, b, x1+row, y1+col)

    def paint(self, name: str):
        ascii_colours = "P3"
        max_colour = 255

        header = f"{ascii_colours} {self.cols} {self.rows} {max_colour} "
        with open(name, 'wt') as handle:
            handle.write(header)
            for lines in self.pixels:
                handle.writelines(lines)


def generate_image(file):
    def sanitize(items: List) -> List:
        return [int(i) if i.isdigit() else i for i in items]

    with open(file, 'rt') as handle:
        lines = (line.strip("\n").split() for line in handle.readlines())
        dimensions = [int(n) for n in next(lines)]
        instructions = [sanitize(line) for line in lines if "#" not in line]

    canvas = Image(dimensions[0], dimensions[1])
    for instruction in instructions:
        func, *args = instruction
        if hasattr(canvas, func):
            getattr(canvas, func)(*args)
    canvas.paint(file.replace(".txt", ".ppm"))


if __name__ == "__main__":
    root = "./data"
    for f in os.listdir(root):
        if f.endswith(".txt"):
            file = os.path.join(root, f)
            print(f"Generating: {file}...")
            generate_image(file)
