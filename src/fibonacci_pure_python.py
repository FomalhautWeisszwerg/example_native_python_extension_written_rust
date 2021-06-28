# coding: utf-8

"""
Caluculate a Fibonacci number using recursive function.

Due to some, it is preferred to avoid the use of recursive functions on CPython interpreter.
    - Performance not good.
    - Lots of stack needed.
    - CPython does not do tail-recursive optimization.

Reference:
    - Fibonacci Number
      https://en.wikipedia.org/wiki/Fibonacci_number
"""

import unittest
import sys

def calculate_fibonacci_number(n : int) -> int:
    """
    Calculate and return the `n` th fibonacci number.

    Args:
        n (int) : specify term.
    
    Exceptions:
        - TypeError: when the type of `n` is not int.
        - ValueError: when `n` is negative.
    
    Note:
        This solution obtains the answer by tracing from the target term to the first term.

        0   1   1   3 ... A(n - 2) A(n - 1) A(n)
                              ↑        ↑      ↓
                              `--------⊥------
    
    WARNING:
        This implementation increases function calls exponentially.
        And this recomputes Fibonacci numbers that have already computed.
    """
    if type(n) != int:
        raise TypeError("`n` MUST be int but {} was passed.".format(type(n)))
    
    if n < 0:
        raise ValueError("`n` MUST be a natural but a negative is passed.")
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (calculate_fibonacci_number(n - 2) + calculate_fibonacci_number(n - 1))


class Test_calculate_fibonacci_number(unittest.TestCase):
    partial_fibonacci_sequence = [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
        17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578,
        5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155
    ]

    def test_non_int_type_passed(self):
        """
        `calculate_fibonacci_number()` raises TypeError when the type of `n` is not int.
        """
        with self.assertRaises(TypeError):
            calculate_fibonacci_number("12")
    
    def test_error_message_with_non_int_type(self):
        """
        `calculate_fibonacci_number()` raises TypeError when the type of `n` is not int.
        And the exception object has a message "`n` MUST be int but {} was passed."
        """
        try:
            calculate_fibonacci_number("12")
        except TypeError as error_object:
            self.assertEqual(
                str(error_object),
                "`n` MUST be int but {} was passed.".format(type("12"))
            )
    
    def test_fibonacci_number(self):
        for fibonacci_number in self.partial_fibonacci_sequence:
            self.assertEqual(
                calculate_fibonacci_number(self.partial_fibonacci_sequence.index(fibonacci_number)),
                fibonacci_number
            )

if __name__ == "__main__":
    if "profiling" in sys.argv:
        calculate_fibonacci_number(50)
    else:
        unittest.main()
