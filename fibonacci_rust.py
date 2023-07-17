"""Fibonacci sequence
Used as load for testing diffrent compiling options. 
"""

from time import time
from rust import fibonacci


def main():
    n = 37
    t_start = time()
    num = fibonacci(n)
    t_end = time()
    print(f"Fibonacci number {n} is {num:>18}")
    print(f"Time to calculate {t_end - t_start:>18.5f}s")

if __name__ == "__main__":
    main()
