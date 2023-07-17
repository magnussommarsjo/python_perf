"""Running påerformance tests

TODO: This measurements with subprocess includes time for imports and starting python instance.

"""

import fibonacci
import fibonacci_numba
from rust import fibonacci as fib_rust

import timeit
import pprint
import subprocess

FIB_SEQUENCE = 37
REPEATS = 1

results = {}


# Regular Python
print("Regular python running...")
results['base'] = timeit.timeit(lambda: fibonacci.fib(FIB_SEQUENCE), number=REPEATS)

# With Numba
print("Numba python running...")
# Note: run numba to pre-compile. Resulting in "hot run"
_ = fibonacci_numba.fib(5)
results['fib_numba'] = timeit.timeit(lambda: fibonacci_numba.fib(FIB_SEQUENCE), number=REPEATS)

# Rust implementation
print("Rust running...")
results['fib_rust'] = timeit.timeit(lambda: fib_rust (FIB_SEQUENCE), number=REPEATS)

# PyPy
print("Pypy running...")
# TODO: Fix iussue with pypy3 stating that timit mofule doesnt exist
# pypy_timit_cmd = f"pypy3 -m timeit --number {REPEATS} --setup 'from fibonacci import fibonacci' 'fibonacci({FIB_SEQUENCE})'"
# pypy_timit_cmd = ["pypy3", "-m timeit", f"--number {REPEATS}", "--setup 'from fibonacci import fibonacci'", f"fibonacci({FIB_SEQUENCE})"]
# res = subprocess.call(pypy_timit_cmd)

# NOTE: this subpricesss also measures imports
def run_pypy():
    subprocess.call(["pypy3", "-c", f"from fibonacci import fib; fib({FIB_SEQUENCE})"])

results['pypy'] = timeit.timeit(lambda: run_pypy(), number=REPEATS)


# Mypy
print("Mypyc running...")
print("Compiling with mypyc...")
subprocess.call(["mypyc", "fibonacci.py"])  # Compile code
print("...compiling finished. Remove folder afterwards")

# NOTE: this subpricesss also measures imports
def run_mypyc():
    subprocess.call(["python3", "-c", f"from fibonacci import fib; fib({FIB_SEQUENCE})"])

results['mypyc'] = timeit.timeit(lambda: run_mypyc(), number=REPEATS)
# importlib.reload(fibonacci)
# results['mypyc'] = timeit.timeit(lambda: fibonacci.fib(FIB_SEQUENCE), number=REPEATS)


pprint.pprint(results)

base = results.pop('base')
print(f"{'python':>10}: {base:.3f},")
for key, value in results.items():
    print(f"{key:>10}: {value:.3f}, {base/value:.2f}x")
