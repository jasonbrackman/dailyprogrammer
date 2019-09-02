from typing import NamedTuple, List
import re
import math

# Regex pattern search to be used multiple times
# Example: #ff0533 -> ff, 05, 33
pattern = re.compile(r'#(?P<r>\w{2})(?P<g>\w{2})(?P<b>\w{2})')


class RGB(NamedTuple):
    r: int
    g: int
    b: int

    @classmethod
    def from_hex(cls, colour: str):
        c = re.match(pattern, colour)
        red = int(c["r"], 16)
        green = int(c["g"], 16)
        blue = int(c["b"], 16)
        return cls(red, green, blue)

    def srgb_to_linear(self) -> List[float]:
        """
        http://davengrace.com/cgi-bin/cspace.pl
        :return:
        """
        values = list()
        a = 0.055
        for value in [self.r, self.g, self.b]:
            value = (value / 255)
            linear_val_small = value / 12.92
            linear_val = math.pow(abs((value + a) / (1 + a)), 2.4)
            values.append(linear_val_small if (value < 0.04045) else linear_val)

        # print(f"Linear Values: ({values[0]}, {values[1]}, {values[2]})")

        return values

    @staticmethod
    def linear_to_srgb(values: List[float]):
        srgbs = list()
        a = 0.055
        for value in values:
            srgb_val_small = value * 12.92
            srgb_val = (1+a) * math.pow(abs(value), 1/2.4) - a
            result = srgb_val_small if (value < 0.0031308) else srgb_val

            srgbs.append(round(result*255))

        # print(f"Perception Values: ({srgbs[0]}, {srgbs[1]}, {srgbs[2]})")

        return RGB(srgbs[0], srgbs[1], srgbs[2])

    def hex(self) -> str:
        red = hex(self.r)
        green = hex(self.g)
        blue = hex(self.b)
        return f"#{red[2:].zfill(2)}{green[2:].zfill(2)}{blue[2:].zfill(2)}".upper()

    @staticmethod
    def blend_hexcodes(colours: set):

        r, g, b = 0.0, 0.0, 0.0

        for colour in colours:
            a, b, c = RGB.from_hex(colour).srgb_to_linear()
            r += a
            g += b
            b += c

        return RGB.linear_to_srgb([
            r / len(colours),
            g / len(colours),
            b / len(colours)
        ])

    def __repr__(self) -> str:
        return f"({self.r}, {self.g}, {self.b}) => {self.srgb_to_linear()} => {self.hex()}"


def hexcolor(r: int, g: int, b: int) -> str:
    color = RGB(r, g, b)
    return color.hex()


def blend(colours: set) -> str:

    red, green, blue = 0, 0, 0

    for colour in colours:
        c = re.match(pattern, colour)
        red += int(c["r"], 16)
        green += int(c["g"], 16)
        blue += int(c["b"], 16)

    return hexcolor(
        # ensuring any weird rounding only happens once
        int(round(red / len(colours))),
        int(round(green / len(colours))),
        int(round(blue / len(colours)))
    )


assert hexcolor(255, 99, 71) == "#FF6347"  # (Tomato)
assert hexcolor(184, 134, 11) == "#B8860B"  # (DarkGoldenrod)
assert hexcolor(189, 183, 107) == "#BDB76B"  # (DarkKhaki)
assert hexcolor(0, 0, 205) == "#0000CD"  # (MediumBlue)

assert blend({"#000000", "#778899"}) == "#3C444C"
assert blend({"#E6E6FA", "#FF69B4", "#B0C4DE"}) == "#DCB1D9"


# -- Additional Exploration w/ Gamma Correction
result1 = RGB.blend_hexcodes({"#000000", "#778899"})
print(f"After Gamma Blend: {result1} and without correction -> #3C444C")

result2 = RGB.blend_hexcodes({"#E6E6FA", "#FF69B4", "#B0C4DE"})
print(f"After Gamma Blend: {result2} and without correction -> #DCB1D9")

result3 = RGB.blend_hexcodes({"#ff0000", "#00ff00"})
print(f"After Gamma Blend: {result3}")

result4 = blend({"#ff0000", "#00ff00"})
print(f"After Blend: {result4}")
