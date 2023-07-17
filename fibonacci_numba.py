"""Fibonacci sequence
Used as load for testing diffrent compiling options. 
"""

from numba import njit


@njit
def fib(n: int) -> int:
    """Simple fibonacci implementation"""
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)

