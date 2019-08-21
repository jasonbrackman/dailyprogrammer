def upc(code: int) -> int:
    digits = [int(n) for n in f"{code}".zfill(11)]
    odds = sum(d for i, d in enumerate(digits) if (i % 2 == 0))
    evens = sum(d for i, d in enumerate(digits) if (i % 2 != 0))
    m = ((odds * 3) + evens) % 10

    return 0 if m == 0 else 10-m


assert upc(4210000526) == 4
assert upc(3600029145) == 2
assert upc(12345678910) == 4
assert upc(1234567) == 0

