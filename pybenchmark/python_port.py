from typing import Sequence, Union
import random

from numpy.typing import NDArray
import numpy as np


def sample_balanced_py(
    symbols: Sequence[Union[int, str]],
    m: int = 1,
    size: int = 1,
    seed: int = -1
) -> NDArray:
    """
    Pure Python implementation of balanced sequence sampler.

    Each of the `size` rows will contain a random shuffle of `symbols` repeated `m` times.
    """
    if not symbols:
        raise ValueError("`symbols` must be a non-empty sequence.")
    if len(set(symbols)) != len(symbols):
        raise ValueError("`symbols` must contain only unique values.")
    if m < 1:
        raise ValueError("`m` must be ≥ 1.")
    if size < 1:
        raise ValueError("`size` must be ≥ 1.")

    if seed >= 0:
        random.seed(seed)

    result = []

    for _ in range(size):
        row = list(symbols) * m
        random.shuffle(row)
        result.append(row)

    return np.array(result, dtype=object if isinstance(symbols[0], str) else type(symbols[0]))


if __name__ == "__main__":
    import time

    symbols = ['a', 'b', 'c', 'd', 'f', 'e', 'g', 'h', 'i', 'j']
    size = 1_000_000
    m = 10
    seed = 42

    print(f"Testing {size:,} simulations with m={m}, seed={seed} using pure Python...")

    start = time.time()
    seq = sample_balanced_py(symbols=symbols, m=m, size=size, seed=seed)
    duration = time.time() - start

    print(f"First 3 rows:\n{seq[:3]}")
    print(f"Took {duration:.4f} sec for {size:,} items")
