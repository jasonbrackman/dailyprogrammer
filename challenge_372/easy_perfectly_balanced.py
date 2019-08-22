
def balanced(characters: str) -> bool:
    if len(characters) == 0:
        return True
    if len(characters) == 1:
        return False

    unique_count = {characters.count(unique) for unique in set(characters)}
    return len(unique_count) == 1


def balanced_bonus(characters: str) -> bool:
    return True if len(characters) == 1 else balanced(characters)


assert balanced("yyyxxx") is True
assert balanced("xxxyyy") is True
assert balanced("xxxyyyy") is False
assert balanced("yyxyxxyxxyyyyxxxyxyx") is True
assert balanced("xyxxxxyyyxyxxyxxyy") is False
assert balanced("") is True
assert balanced("x") is False

assert balanced_bonus("xxxyyyzzz") is True
assert balanced_bonus("abccbaabccba") is True
assert balanced_bonus("xxxyyyzzzz") is False
assert balanced_bonus("abcdefghijklmnopqrstuvwxyz") is True
assert balanced_bonus("pqq") is False
assert balanced_bonus("fdedfdeffeddefeeeefddf") is False
assert balanced_bonus("www") is True
assert balanced_bonus("x") is True
assert balanced_bonus("") is True