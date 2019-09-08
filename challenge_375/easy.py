from typing import List


# Original problem
def new_number_using_strings(num: int) -> int:
    return int(
        ''.join([str(int(n) + 1) for n in str(num)])
    )


# Bonus
def new_number(num: int) -> int:
    results = break_down(num)
    result = build_up(results)
    return result


def break_down(number: int) -> List[int]:
    results = list()

    while number > 9:
        results.append(number)
        number //= 10

    results.append(number)

    final = list()
    for result in results:
        if result > 9:
            final.append(result - (result // 10) * 10)
        else:
            final.append(result)

    return final


def build_up(numbers: List[int]) -> int:
    num = 0

    factor = 1
    for result in numbers:
        result += 1
        num += result * factor

        # Increase factor for next run
        factor = factor * 100 if result == 10 else factor * 10

    return num

