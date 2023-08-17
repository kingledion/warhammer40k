import re
import numpy as np

from rules.rolls import *

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


ptrn = re.compile("(\d*)(d3|d6)(?:\+(\d+))*")
def parse_variable(x: str):
    m = re.match(ptrn, x)
    a, b, c = m.group(1, 2, 3)
    a = int(a) if a else 1
    c = int(c) if c else 0
    return a, b, c


def resolve_variable(x: int | str) -> int:
    if isinstance(x, int):
        return x
    
    if not isinstance(x, str):
        raise Exception("Invalid type for datasheet value {x}")
    
    a, b, c = parse_variable(x)
    match b:
        case 'd3':
            return np.sum(d3(a)) + c
        case 'd6':
            return np.sum(d6(a)) + c
    

    
