def limit_1(adj: int) -> int:
    if adj > 1:
        return 1
    if adj < -1:
        return -1
    return adj

def ceiling_1(adj: int) -> int:
    if adj > 1:
        return 1
    return adj