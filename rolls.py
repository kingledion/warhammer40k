import random

def d6(cnt: int = 1) -> list[int]:
    return [random.randint(1, 6) for _ in range(cnt)]


def d3(cnt: int = 1) -> int:
    return [random.randint(1, 3) for _ in range(cnt)]
