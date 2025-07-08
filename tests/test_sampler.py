import time

from sampler import sample_balanced


symbols = ['a', 'b', 'c']
size = 1_000_000
seed = 42
m = 3

start = time.time()
seq = sample_balanced(symbols=symbols, m=m, size=size, seed=42)
end = time.time()

print("First 10 rows...")
print(seq[:10, :])
print(f"Took {end - start:.4f} sec for {size} items")
