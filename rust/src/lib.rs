use pyo3::prelude::*;

/// Simple fibonacci implementation in Rust
#[pyfunction]
fn fibonacci(n: usize) -> PyResult<usize> {
    let res = fib(n);
    Ok(res)
}

fn fib(n: usize) -> usize {
    if n <= 1 {
        return n;
    }
    return fib(n-1) + fib(n - 2);
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fibonacci, m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_fib() {
        assert_eq!(1, fib(2));
        assert_eq!(21, fib(8));
    }

}