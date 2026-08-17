# MPI Sorting Benchmark

CA Assignment — Parallel & Grid Computing, Year 4, BSc Computer Science.

An MPI benchmark comparing four parallel sorting algorithms — Direct, Bucket, Odd-Even and Shell — across different core counts. Each algorithm scatters a large random array, sorts locally with merge sort, exchanges and merges across ranks, and reports communication vs processing time.

## Files

| File | Description |
|------|-------------|
| `sorting.c` | MPI implementations of the four sorting algorithms with timing |
| `Makefile` | Builds with `mpicc` |
| `plot_results.py` | Plots execution/communication/processing time and speedup vs core count |

## Usage

```bash
make
mpirun -np 4 ./sorting

pip install -r requirements.txt
python3 plot_results.py
```

Requires an MPI implementation (e.g. OpenMPI) and Python for the plotting.
