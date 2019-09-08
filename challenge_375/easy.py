from typing import List


# Original problem
def new_number_using_strings(num: int) -> int:
    return int(
        ''.join([str(int(n) + 1) for n in str(num)])
    )


# Bonus
def new_number(number: int) -> int:
    return_total = 0

    factor = 1
    while number > 9:
        result = get_right_most_digit_plus_one(number)
        return_total += result * factor

        # Calc values for next loop
        factor = factor * 100 if result == 10 else factor * 10
        number //= 10

    result = get_right_most_digit_plus_one(number)
    return_total += result * factor

    return return_total


def get_right_most_digit_plus_one(digit: int) -> int:
    return (digit - (digit // 10) * 10) + 1


print(new_number(1234))
