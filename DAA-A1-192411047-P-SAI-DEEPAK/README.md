# DAA Assignment 1: Student Record Search

**Name:** P SAI DEEPAK  
**Registration Number:** 192411047

## Algorithms
1. Linear search (iterative, no preprocessing).
2. Recursive binary search (requires sorted records; sorting cost is measured separately).
3. Hash index lookup (build a hash set once, then expected constant-time lookups).

## Requirements
- Python 3.10 or later
- Matplotlib and pandas are only needed to regenerate the report plots; the core benchmark uses the Python standard library.

## Run
From the repository root:

```bash
python src/dataset_generator.py
python src/benchmark.py
python src/make_graphs.py
```

The benchmark generates deterministic datasets from the last four digits of the registration number (seed 1047), tests the student's registration number as present and registration number + 1 as absent, and writes `results/results.csv` plus `results/challenge_summary.txt`.

## Results and evidence
- `results/results.csv`: measured timings and operation counts.
- `results/graphs/`: plots generated from the CSV.
- `screenshots/`: place genuine full terminal screenshots here. The assignment rules require the system date/time and student name or registration number to be visible. Do not substitute generated mock screenshots for actual terminal captures.
- `report/DAA_A1_192411047.pdf`: assignment report.

## Important
Runtime values depend on the machine and must be regenerated on the computer used for submission. The report labels measured values as local benchmark results. Take actual screenshots after running the commands above, then commit them. The third strategy is hash indexing; verify whether your instructor assigned a different third-strategy group.
