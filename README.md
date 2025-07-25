# ⚖️ SamplePlan — Nim-Powered Balanced Sampler for Python

[![PyPI version](https://img.shields.io/pypi/v/sampleplan.svg?logo=pypi)](https://pypi.org/project/sampleplan/)

A blazing-fast compiled backend for generating balanced random sequences in
Python. Built using [Nim](https://nim-lang.org/) and exposed via `ctypes`.
Ideal for simulations, experimental design, or randomized testing scenarios
where equal representation of categories is required.

## 🚧 Note

> This is a lightweight, low-level library that demonstrates how to integrate
> compiled Nim code with Python. It exposes a single high-performance utility
> for generating balanced permutations, useful in simulation, randomization,
> and probabilistic workflows.

## 🚀 Features

- ⚡ Fast compiled DLL backend (Nim → C → Python)
- 📦 Seamless Python interface via `ctypes`
- 🧮 Returns balanced permutations of symbols
- 🧪 Deterministic output with `seed`

## 📦 Setup

Install Python and [Nim](https://nim-lang.org/) if you intend to rebuild the
shared library from source.

Create your virtual environment:

```bash
python -m venv venv
```

Then activate it:

```bash
venv\Scripts\activate
```

Install the project's dependencies from the requirements file, if any:

```bash
python -m pip install -r requirements.txt
```

## 🐍 Python Usage

Install the local package:

```bash
python -m pip install -e .
```

Then use it. This call returns a `3 × 6` NumPy array (3 simulations of 2 × 3
symbols):

```python
from sampleplan import sample_balanced

out = sample_balanced(["A", "B", "C"], m=2, size=3, seed=42)
print(out)
# array([
#   ['A', 'B', 'C', 'C', 'B', 'A'],
#   ['B', 'C', 'A', 'A', 'B', 'C'],
#   ['C', 'A', 'B', 'B', 'C', 'A']
# ])
```

## 🧱 Underlying C Signature

This function accepts raw memory buffers from Python and writes directly into
the pre-allocated output array. It is not meant to be called directly from user
code.

```c
void sampleBalanced(
    int* symbols, int symbolCount, int m, int size, int seed, int* outSeq
);
```

All pointer data is managed from the Python side using NumPy and ctypes.

## 🏗️ Build the DLL (Windows)

Compile the DLL using the Nim compiler and Microsoft's Visual C++ (MSVC)

```bash
nim c --cc:vcc --app:lib --out:sampler/sampleplan.dll nimsrc/sampleplan.nim
```

For faster release builds:

```bash
nim c --cc:vcc --app:lib --out:sampleplan/sampleplan.dll -d:release nimsrc/sampleplan.nim
```

This generates `sampleplan.dll`, which is required for Python execution.

## 📦 Packaging and Distribution

To build the Python wheel:

```bash
python -m build --wheel
```

## 📁 Project Structure

```bash
sampleplan/
├── __init__.py
├── sampleplan.py            # Python interface to the DLL
├── sampleplan.dll           # Compiled Nim shared library
nimsrc/
└── sampleplan.nim           # Nim source code (not distributed)
tests/
└── test_sampler.py
pyproject.toml
LICENSE
MANIFEST.in
README.md
```

## ⚠️ Platform Support

- ✅ Windows
- ⏳ Linux and macOS coming soon

## 🧠 License

MIT — use freely, cite kindly. See [LICENSE](LICENSE).

## 📜 Changelog

### [0.1.0] — Initial Release

- First public version of `sampleplan`
- Exposes `sample_balanced()` via a compiled Nim DLL
- Supports any unique sequence of symbols (str/int)
- Deterministic sampling with `seed`
- 1D or 2D NumPy output based on `size` argument

### [0.1.1] — 2025-07-11

- Improved and clarified `README.md` formatting
- Added Changelog section to `README.md`
- Declared GitHub metadata in `pyproject.toml`
- Removed unnecessary exclusions from `.gitignore`
- Restored previously unversioned Nim source file `sampleplan.nim`
- Refined reformatting in `test_sampler.py`
