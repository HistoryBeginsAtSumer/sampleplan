import time

from sampleplan import sample_balanced


def main():
    """Run a high-volume benchmark to test runtime performance."""
    symbols = ['a', 'b', 'c', 'd', 'f', 'e', 'g', 'h', 'i', 'j']
    size = 1_000_000
    m = 10
    seed = 42

    print(f"Testing {size:,} simulations with m={m}, seed={seed}...")

    start = time.time()
    seq = sample_balanced(symbols=symbols, m=m, size=size, seed=seed)
    duration = time.time() - start

    assert seq.shape == (size, len(symbols) * m), "Shape mismatch"
    assert sorted(seq[0].tolist()) == sorted(symbols * m), "First row not balanced"

    print(f"First 3 rows:\n{seq[:3]}")
    print(f"Took {duration:.4f} sec for {size:,} items")


if __name__ == "__main__":
    main()
