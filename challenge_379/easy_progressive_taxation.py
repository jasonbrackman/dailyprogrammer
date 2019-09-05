#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

CAP_RATE = {
    10_000: 0,
    30_000: 0.1,
    100_000: 0.25,
    "default": 0.4,
}


def tax(num: int) -> int:
    if num == 0:
        return 0

    bracket_old = 0
    total_tax = 0

    # First go through all the layers, except for the max
    for k, v in CAP_RATE.items():
        if isinstance(k, int):
            # Is num large enough to warrant a tax?
            temp_ = num-bracket_old if num-bracket_old > 0 else 0

            # Ensure the bracket is taxed, anything over is ignored
            if temp_ + bracket_old >= k:
                temp_ = k - bracket_old

            # Apply the tax
            total_tax += temp_ * v

        bracket_old = k if isinstance(k, int) else bracket_old

    # Did the user hit the max tax rate?  It must be above the last known bracket_old...
    whats_left = num - bracket_old
    if whats_left > 0:
        total_tax += (whats_left * CAP_RATE["default"])

    return int(total_tax)


def overall(tax_rate: float) -> int:
    start = next(iter(CAP_RATE.keys()))
    if tax_rate <= CAP_RATE[start]:
        return start

    for x in range(10_000, 500_000):
        t = tax(x)
        rate = t/x

        if math.isclose(round(rate, 5), tax_rate):
            return x

    return -1
