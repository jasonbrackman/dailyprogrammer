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
        result = (number - (number // 10) * 10) + 1
        return_total += result * factor

        # Calc values for next loop
        factor = factor * 100 if result == 10 else factor * 10
        number //= 10

    result = (number - (number // 10) * 10) + 1
    return_total += result * factor

    return return_total


if __name__ == "__main__":
    import timeit
    number = 102030405060708090
    print(timeit.timeit(lambda: new_number_using_strings(number), number=100_000))
    print(timeit.timeit(lambda: new_number(number), number=100_000))

    # import cProfile
    # cProfile.run("timeit.timeit(lambda: new_number_using_strings(102030405060708090), number=1_000)")
    # cProfile.run("timeit.timeit(lambda: new_number(102030405060708090), number=1_000)")
