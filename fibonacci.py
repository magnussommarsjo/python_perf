"""Fibonacci sequence
Used as load for testing diffrent compiling options. 
"""

from time import time


def fibonacci(n: int) -> int:
    """Simple fibonacci implementation"""
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


def main():
    n = 37
    t_start = time()
    num = fibonacci(n)
    t_end = time()
    print(f"Fibonacci number {n} is {num:>18}")
    print(f"Time to calculate {t_end - t_start:>18.3f}s")

if __name__ == "__main__":
    main()
