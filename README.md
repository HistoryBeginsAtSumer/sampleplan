# Nim Python Lib

This exposes a single function:

```c
void sampleBalanced(int* symbols, int symbolCount, int m, int* outSeq)
```

Compile to Shared Library:

```sh
nim c --cc:vcc --app:lib --out:sampler/sampler.dll build/sampler.nim
```

Note: `-d:release` generates faster code:

```sh
nim c --cc:vcc --app:lib --out:sampler/sampler.dll -d:release build/sampler.nim
```

Install the local package:

```sh
pip install -e .
```
