#!/usr/bin/python3
"""
Module for calculating factorial recursively.
"""
import sys

def factorial(n):
    """
    Calculates the factorial of a given number recursively.

    Parameters:
        n (int): The non-negative integer to compute the factorial for.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = factorial(int(sys.argv[1]))
        print(f)
