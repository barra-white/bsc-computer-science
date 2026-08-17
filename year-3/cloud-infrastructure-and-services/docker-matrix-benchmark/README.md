# Docker Matrix Benchmark

Lab 1 — Cloud Infrastructure & Services (CS3204), Year 3, BSc Computer Science.

Benchmarks an N×N matrix multiplication workload across three environments — bare-metal laptop, VirtualBox VM, and a Docker container — and plots average runtime against matrix size.

## Files

| File | Description |
|------|-------------|
| `program.py` | Generates random N×N matrices and times multiplication (runs inside the container) |
| `plot_results.py` | Plots the collected laptop / VirtualBox / Docker runtimes with matplotlib |
| `results.txt` | Raw runtime results |
| `Dockerfile` | Builds the benchmark container image |

## Usage

```bash
docker build -t matrix-benchmark .
docker run matrix-benchmark

pip install -r requirements.txt
python3 plot_results.py
```
