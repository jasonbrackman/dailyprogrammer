import math
import os
from typing import List


class Canvas:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.pixels = list()
        # Default background is black
        self.fill(0, 0, 0)

    def fill(self, r: int, g: int, b: int) -> None:
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
        """"""
        results = [(x1, y1)]

        current = (x1, y1)
        while (x2, y2) not in results:
            _x, _y = current

            # set current to a large num.
            current_values = (1_000_000_000, ())
            for i in (_x-1,_x, _x+1):
                for j in (_y-1, _y, _y+1):
                    if i >= 0 and j >= 0:
                        if (i, j) not in results and (i, j) != (_x, _y):
                            v = self.euclidean_distance(i, j, x2, y2)
                            if v < current_values[0]:
                                current_values = (v, (i, j))

            current = current_values[1]
            if current:
                results.append(current)

        for item in results:
            self.point(r, g, b, item[0], item[1])

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
        instructions = [sanitize(line) for line in lines]

    canvas = Canvas(dimensions[0], dimensions[1])
    for instruction in instructions:
        getattr(canvas, instruction[0])(*instruction[1:])
    canvas.paint(file.replace(".txt", ".ppm"))


if __name__ == "__main__":
    root = "./data"
    for f in os.listdir(root):
        if f.endswith(".txt"):
            file = os.path.join(root, f)
            print(f"Generating: {file}...")
            generate_image(file)
