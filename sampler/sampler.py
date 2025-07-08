# sampler.py
from typing import Sequence, Union
import platform
import ctypes
import os

from numpy.typing import NDArray
import numpy as np


# Load shared library
ext = {'Windows': 'dll', 'Linux': 'so', 'Darwin': 'dylib'}[platform.system()]
this_dir = os.path.dirname(__file__)
libname = os.path.join(this_dir, f'sampler.{ext}')
lib = ctypes.CDLL(libname)

# Function signature
lib.sampleBalanced.argtypes = [
    ctypes.POINTER(ctypes.c_int),  # symbols
    ctypes.c_int,                  # symbolCount
    ctypes.c_int,                  # m
    ctypes.c_int,                  # size
    ctypes.c_int,                  # seed
    ctypes.POINTER(ctypes.c_int)   # outSeq
]

lib.sampleBalanced.restype = None


def sample_balanced(
    symbols: Sequence[Union[int, str]], m: int = 1, size: int = 1,
    seed: int = -1
) -> NDArray:
    if not symbols:
        raise ValueError("`symbols` must be a non-empty sequence.")

    if len(set(symbols)) != len(symbols):
        raise ValueError("`symbols` must contain only unique values.")

    if size < 1:
        raise ValueError(
            f"`size` must be a positive integer, got value `{size}`."
        )

    if m < 1:
        raise ValueError(
            f"`m` must be a positive integer, got value `{m}`."
        )

    symbols = np.asarray(symbols)
    n = len(symbols)
    encoded = np.arange(n, dtype=np.int32)
    output = np.empty(n * m * size, dtype=np.int32)

    lib.sampleBalanced(
        encoded.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
        len(symbols),
        m,
        size,
        seed,
        output.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
    )

    decoded = symbols[output]

    if size == 1:
        return decoded.reshape(n * m)

    return decoded.reshape(size, n * m)
