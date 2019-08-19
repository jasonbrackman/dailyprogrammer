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

    def linear_srgb(self) -> List[float]:
        """
        http://davengrace.com/cgi-bin/cspace.pl
        :return:
        """
        # (n / 255) ^ 2.2 (convert to linear)
        rl = (self.r / 255) ** 2.2
        gl = (self.g / 255) ** 2.2
        bl = (self.b / 255) ** 2.2
        # print(f"Linear Values: ({rl}, {gl}, {bl})")

        # n ^ 0.4545 (convert to linear sRGB float)
        rs = rl ** 0.4545
        gs = gl ** 0.4545
        bs = bl ** 0.4545

        # final Corrected values
        values = list()
        for s in [rs, gs, bs]:
            values.append(s / 12.92 if s <= 0.04045 else (math.pow((s + 0.055) / 1.055, 2.4)))

        print(f"sRGB Linear Values: ({values[0]}, {values[1]}, {values[2]})")

        return values

    def hex(self) -> str:
        red = hex(self.r)
        green = hex(self.g)
        blue = hex(self.b)
        return f"#{red[2:].zfill(2)}{green[2:].zfill(2)}{blue[2:].zfill(2)}".upper()

    def __repr__(self) -> str:
        hex_conversion = self.hex()
        return f"({self.r}, {self.g}, {self.b}) => {hex_conversion}"


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

# ----- Exploring a bit more ...

# From original sRGB8bit gamma corrected values
x = RGB(255, 127, 240)

# Convert to linear space
r = x.linear_srgb()

# Convert back to sRGB gamma corrected
# -- If I've understood this properly -- which may not be the case.
test = math.pow(r[1], 1/2.2) * 255
print(test)

