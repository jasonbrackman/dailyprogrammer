
def format_input(text):
    info = text.splitlines()
    values = sorted([int(v) for v in info[1].split() if v.isdigit()], reverse=True)
    queries = [int(v) for v in info[2].split() if v.isdigit()]
    return queries, values


def get_results(queries, values) -> dict:

    results = dict()

    for query in queries:
        pass01 = [1 for v in values if v >= query]
        pass02 = [v for v in values if v < query]

        while pass02:
            current = pass02.pop(0)
            count = query - current
            current_len = len(pass02)
            if current_len >= count:
                for _ in range(count):
                    eat = pass02.pop()
                    # print(f"[{query}]: {current} is Eating {eat}")
                pass01.append(1)
            else:
                break

        results[query] = pass01

    return results


def main():
    input_ = """7 2
        21 9 5 8 10 1 3
        10 15
        """
    queries, values = format_input(input_)
    results = get_results(queries, values)
    assert len(results[10]) == 4
    assert len(results[15]) == 2


if __name__ == "__main__":
    main()
