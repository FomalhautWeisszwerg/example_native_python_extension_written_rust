use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[allow(unused_variables)]
#[pymodule]
fn fibonacci_number(py: Python, python_module: &PyModule) -> PyResult<()> {
    python_module.add_wrapped(wrap_pyfunction!(get_recursively))?;
    Ok(())
}


#[pyfunction]
fn get_recursively(n: u64) -> PyResult<u64> {
    fn entity(n: u64) -> u64 {
        match n {
            0 => 0,
            1 => 1,
            _ => entity(n - 2) + entity(n - 1)
        }
    }

    let fibonacci_number = entity(n);
    return Ok(fibonacci_number);
}
