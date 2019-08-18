from typing import NamedTuple
import re


class RGB(NamedTuple):
    r: int
    g: int
    b: int

    def hex(self) -> str:
        red = hex(self.r)
        green = hex(self.g)
        blue = hex(self.b)
        return f"#{red[2:].zfill(2)}{green[2:].zfill(2)}{blue[2:].zfill(2)}".upper()

    def __repr__(self) -> str:
        hex_conversion = self.hex()
        return f"({self.r}, {self.g}, {self.b}) => {hex_conversion}"


def hexcolor(r: int, g: int, b: int):
    color = RGB(r, g, b)
    return color.hex()


# Regex pattern search to be used multiple times
# Example: #ff0533 -> ff, 05, 33
pattern = re.compile(r'#(?P<r>\w{2})(?P<g>\w{2})(?P<b>\w{2})')


def blend(colours: set) -> str:

    red = 0
    green = 0
    blue = 0
    for colour in colours:
        c = re.match(pattern, colour)
        c = c.groupdict()
        red += int(c["r"], 16)
        green += int(c["g"], 16)
        blue += int(c["b"], 16)

    result = RGB(
        int(round(red / len(colours))),
        int(round(green / len(colours))),
        int(round(blue / len(colours)))
    )

    return result.hex()


assert hexcolor(255, 99, 71) == "#FF6347"  # (Tomato)
assert hexcolor(184, 134, 11) == "#B8860B"  # (DarkGoldenrod)
assert hexcolor(189, 183, 107) == "#BDB76B"  # (DarkKhaki)
assert hexcolor(0, 0, 205) == "#0000CD"  # (MediumBlue)

assert blend({"#000000", "#778899"}) == "#3C444C"
assert blend({"#E6E6FA", "#FF69B4", "#B0C4DE"}) == "#DCB1D9"


