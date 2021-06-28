AC_PREREQ([2.69])
AC_INIT([Sample of a native Python extension module with Rust.], [0.1.0], [https://chiselapp.com/user/FomalhautWeisszwerg/repository/fibonacci_sequence/ticket])
AC_CONFIG_MACRO_DIR([./m4])

# Checks for programs.
AC_PROG_CC

AC_CHECK_PROGS(CARGO, ["cargo" "${HOME}/.cargo/bin/cargo" "/usr/bin/cargo"], "no")
if test "${CARGO}" = "no"; then
	AC_MSG_RESULT([FATAL: `cargo` not found.])
	AC_MSG_RESULT([Please install Rust and re-run configure.])
	AC_MSG_RESULT([To install Rust, see https://www.rust-lang.org/tools/install])
	exit -1;
fi

AC_CHECK_PROGS(RUSTC, ["rustc" "${HOME}/.cargo/bin/rustc" "/usr/bin/rustc"], "no")
if test "${RUSTC}" = "no"; then
	AC_MSG_RESULT([FATAL: `rustc` not found.])
	AC_MSG_RESULT([Please install Rust and re-run configure.])
	AC_MSG_RESULT([To install Rust, see https://www.rust-lang.org/tools/install])
	exit -1;
fi

AC_CHECK_PROGS(PYTHON, ["python3" "python" "/usr/local/bin/python3" "/usr/bin/python3"], "no")
if test "${PYTHON}" = "no"; then
	AC_MSG_RESULT([FATAL: Python not found.])
	exit -1;
fi

PYTHON_MAJOR_VERSION=`${PYTHON} -c "print(__import__('sys').version_info.major)"`
PYTHON_MINOR_VERSION=`${PYTHON} -c "print(__import__('sys').version_info.minor)"`
PYTHON_MICRO_VERSION=`${PYTHON} -c "print(__import__('sys').version_info.micro)"`
if test ${PYTHON_MAJOR_VERSION} -lt 3; then
	AC_MSG_RESULT([FATAL: Python 3 required.])
	exit -1;
else
	if test ${PYTHON_MINOR_VERSION} -lt 6; then
		AC_MSG_RESULT([FATAL: Python 3.6 or later required.])
		exit -1;
	else
		AC_MSG_RESULT([checking for python3 version... ${PYTHON_MAJOR_VERSION}.${PYTHON_MINOR_VERSION}.${PYTHON_MICRO_VERSION}])
	fi
fi

AC_CHECK_PROGS(PIP, ["pip3" "pip" "${HOME}/.local/bin/pip3" "${HOME}/.local/bin/pip" "/usr/local/bin/pip3" "/usr/local/bin/pip" "/usr/bin/pip3" "/usr/bin/pip"], "no")
if test ${PIP} = "no"; then
	AC_MSG_RESULT([FATAL: `pip` not found.])
	exit -1;
fi

AC_CHECK_PROGS(MATURIN, ["maturin" "${HOME}/.local/bin/maturin" "/usr/local/bin/maturin" "/usr/bin/maturin"], "no")
if test ${MATURIN} = "no"; then
	AC_MSG_RESULT([FATAL: `maturin` not found.])
	AC_MSG_RESULT([Please install `maturin` with `pip` and re-run configure.])
	exit -1;
fi


# Checks for libraries.

# Checks for header files.

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
