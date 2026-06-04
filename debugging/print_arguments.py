#!/usr/bin/python3
"""
Module for printing command-line arguments.
This script prints all arguments passed to it, excluding the script name.
"""
import sys


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(arg)
