# Performance test diffrent speedup solutions

## Fibonacci

Simple code example where we calculate a fibonacci sequence where we calculate run time of number 37

Summary of results.

||Run time [s]|Speed improvement|
|---|---|---|
|Python 3.11| 4.553 | 1x *(baseline)*|
|mypyc|0.49*| 9.3x|
|pypy *(python 3.9.16)*| 0.562* | 8.1x |
|numba *(hot run)*|0.215 | 21.2x |
|rust *(via maturin)*|0.107 | 42.4x |

*\* includes import statements in runtime*

### Regular python

Calculation of `37` fibonacci number took about 4.5 seconds.

```bash
python3 fibonacci.py
```

### Mypyc

With type annotations we can speed up the code.
Running

Installing:

```bash
pip install mypy
```

Compiling:

```bash
mypyc fibonacci.py
```

Will compile the code into c-extensions.
resulting in runtime of ~0.41 s.

Running this c-extentions is done with the following method.

```bash
python -c "from fibonacci import main; main()"
```

### Pypy

JIT compiler for python.

Installation:

```bash
sudo apt install pypy3
```

Then simply run:
```bash
pypy3 fibonacci.py
```

### Numba
JIT compiler for functions

```bash
pip install numba
```

Simply annotate function

```python
from numba import njit

@njit
def fibonacci(n: int) -> int:
    ...

```

And run as regular python

```bash
python3 fibonacci_numba.py
```

### rust
Running an rust implementation with python binfings via maturin and pyo3. 

Assuming that you already have rust set up runnign the following will create the python implementation.
```bash
pip install maturin
cd rust
maturin develop -r
```

Now we can run the code
```bash
python3 fibonacci_rust.py
```
