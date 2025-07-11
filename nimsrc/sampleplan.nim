## sampleplan.nim — Fast balanced sequence sampler (Nim DLL for Python ctypes)
import random

## Export configuration for shared library compatibility
{.push dynlib, exportc, cdecl.}

## Fills `outSeq` with `size` independent simulations.
## Each simulation is a shuffled, balanced sequence of `symbols`, repeated `m` times.
##
## Parameters:
## - symbols: Pointer to array of `symbolCount` values
## - symbolCount: Number of distinct symbols (must be ≥ 1)
## - m: Repetition count per symbol (must be ≥ 1)
## - size: Number of simulations (must be ≥ 1)
## - seed: RNG seed (use -1 for random)
## - outSeq: Pre-allocated output buffer of length `symbolCount * m * size`
proc sampleBalanced(
    symbols: ptr int32,
    symbolCount: int32,
    m: int32,
    size: int32,
    seed: int32,
    outSeq: ptr int32
) =
    if symbolCount <= 0 or m <= 0 or size <= 0:
        return  # silently ignore invalid input

    if seed >= 0:
        randomize(seed)

    let symArray = cast[ptr UncheckedArray[int32]](symbols)
    let outArray = cast[ptr UncheckedArray[int32]](outSeq)
    let rowLength = symbolCount * m

    for sim in 0..<size:
        var pool = newSeq[int32](rowLength)
        var k = 0

        for i in 0..<symbolCount:
            for _ in 0..<m:
                pool[k] = symArray[i]
                inc k

        shuffle(pool)

        let offset = sim * rowLength
        for i in 0..<rowLength:
            outArray[offset + i] = pool[i]

{.pop.}

when isMainModule:
    discard  # DLLs are not runnable directly
