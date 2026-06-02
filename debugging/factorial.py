#!/usr/bin/python3
"""
Module for factorial computation.
This module provides a function to calculate the factorial of a given number,
demonstrating basic debugging to fix an infinite loop issue.
"""
import sys


def factorial(n):
    """
    Calculate the factorial of a positive integer.

    Args:
        n (int): The number to compute the factorial for.

    Returns:
        int: The factorial of the number.
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = factorial(int(sys.argv[1]))
        print(f)
