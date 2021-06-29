# About

This is a tiny example for creating native Python extension modules written in Rust.

These implementations of the Fibonacci sequence is not efficient, but it seems to good for seeing the difference in performance.

# Prerequisite

## [Python](https://www.python.org/downloads/)

CPython 3.6 or later required.


## [Rust](https://www.rust-lang.org/tools/install)

Rust 1.41 or later required.

If you use out-of-dated versions, please run `rustup check && rustup update` in your terminal.

## [PyO3](https://github.com/PyO3/pyo3)

PyO3 is a Rust bindings for Python.

This sample requires version 0.13.2 or later but you might not to need to install PyO3 manually.
Because PyO3 is automatically pulled and prepared by `cargo` at building time.


## [maturin](https://github.com/PyO3/maturin)

'maturin' is a Zero configuration build tool for Rust-made Python extensions.
And requires maturin >= 0.10.0,< 0.11.

If you have not installed this yet, run `pip install --user maturin` in your terminal.


# Build

After checkout, run following commands at the top directory:

```shell
$ autoconf
$ ./configure
$ make
```

# Compare the performance of a pure Python implementation and a native Python Extension implementation.

After build, run:

```shell
$ make profiling
```

Then following are shown

```shell
$ make profiling
cd examples && python3 -m cProfile fibonacci_accelerate.py profiling
         110 function calls in 220.439 seconds

... (snip) ...

cd examples && python3 -m cProfile fibonacci_pure_python.py profiling
         40730028398 function calls (6144 primitive calls) in 36677.990 seconds

... (snip) ...
```


# Try native Python extension without install .whl

After build, `cd examples` and run a Python interpreter.
[IPython](https://pypi.org/project/ipython/) is highly recommended.

```ipython
$ ipython3
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.25.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import fibonacci_number

In [2]: fibonacci_number.get_recursively(10)
Out[2]: 55
```
