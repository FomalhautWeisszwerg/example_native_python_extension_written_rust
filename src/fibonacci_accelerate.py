# coding: utf-8

import sys

import fibonacci_number

if __name__ == "__main__":
    if "profiling" in sys.argv:
        # call with `cProfile` module like `python3 -m cProfile FILE_NAME profiling`
        fibonacci_number.get_recursively(50)
    else:
        for term in range(0, 11):
            print(fibonacci_number.get_recursively(term))

