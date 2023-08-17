import numpy as np
import numpy.typing as npt
from typing import Sequence

def d6(n: int | Sequence[int]) -> npt.NDArray:
    return np.random.randint(1, 7, n)

def d3(n: int | Sequence[int]) -> npt.NDArray:
    return np.random.randint(1, 4, n)