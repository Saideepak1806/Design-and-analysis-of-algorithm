import csv, sys, time, random, platform, datetime
from pathlib import Path
from algo1_linear_search import linear_search
from algo2_binary_search import binary_search_recursive
from algo3_hash_search import build_hash_index, hash_search
from dataset_generator import generate_records, SEED, REG_NO

SIZES = [1_000, 10_000, 100_000, 1_000_000]
REPEATS = 5

def timed(fn):
    t0 = time.perf_counter()
    result = fn()
    return result, time.perf_counter() - t0

def main():
    print("=" * 78)
    print(f"Reg No: {REG_NO} | Name: P SAI DEEPAK")
    print("DAA Assignment 1 | Local benchmark | " + datetime.datetime.now().astimezone().isoformat(timespec="seconds"))
    print(f"Python: {sys.version.split()[0]} | Platform: {platform.platform()} | Seed: {SEED}")
    print("=" * 78)
    rows = []
    for n in SIZES:
        records = generate_records(n)
        sorted_records = sorted(records)
        # Personal search key is guaranteed present; reg no + 1 is guaranteed absent.
        found_key = int(REG_NO)
        absent_key = int(REG_NO) + 1
        assert found_key in records and absent_key not in records
        # Build index and measure preprocessing separately.
        hash_index, hash_build_s = timed(lambda: build_hash_index(records))
        _, sort_s = timed(lambda: sorted(records))
        queries = [found_key, absent_key]
        # Use absent key for predictable worst-case linear scan; found key also tested.
        lin_counts = {}
        lin_time, lin_comps = 0.0, 0
        for key in queries:
            c = {}
            _, elapsed = timed(lambda: linear_search(records, key, c))
            lin_time += elapsed
            lin_comps += c.get("comparisons", 0)
        bin_counts = {}
        bin_time, bin_comps = 0.0, 0
        for key in queries:
            c = {}
            _, elapsed = timed(lambda: binary_search_recursive(sorted_records, key, counter=c))
            bin_time += elapsed
            bin_comps += c.get("comparisons", 0)
        hash_time = 0.0
        for key in queries:
            _, elapsed = timed(lambda: hash_search(hash_index, key))
            hash_time += elapsed
        # repeat timing for more stable display; comparison counts remain deterministic.
        rows.extend([
            {"n": n, "algorithm": "Linear search", "preprocessing_seconds": 0.0, "search_seconds_2_queries": lin_time, "comparisons_2_queries": lin_comps, "total_seconds": lin_time, "test_cases": "found own reg; absent reg+1"},
            {"n": n, "algorithm": "Recursive binary search", "preprocessing_seconds": sort_s, "search_seconds_2_queries": bin_time, "comparisons_2_queries": bin_comps, "total_seconds": sort_s + bin_time, "test_cases": "found own reg; absent reg+1"},
            {"n": n, "algorithm": "Hash index lookup", "preprocessing_seconds": hash_build_s, "search_seconds_2_queries": hash_time, "comparisons_2_queries": "not directly comparable", "total_seconds": hash_build_s + hash_time, "test_cases": "found own reg; absent reg+1"},
        ])
        print(f"n={n:>7,} | linear: {lin_time:.6f}s / {lin_comps} comparisons | binary: {bin_time:.6f}s / {bin_comps} comparisons (sort {sort_s:.6f}s) | hash: {hash_time:.6f}s (build {hash_build_s:.6f}s)")
        # correctness checks for every algorithm
        assert linear_search(records, found_key) != -1
        assert linear_search(records, absent_key) == -1
        assert binary_search_recursive(sorted_records, found_key) != -1
        assert binary_search_recursive(sorted_records, absent_key) == -1
        assert hash_search(hash_index, found_key) == found_key
        assert hash_search(hash_index, absent_key) is None
    out = Path("results/results.csv")
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)
    # Challenge: 50,000 queries on 1M records; measure query throughput for hash index and binary search.
    n = 1_000_000
    records = generate_records(n)
    sorted_records = sorted(records)
    index, build_s = timed(lambda: build_hash_index(records))
    rng = random.Random(SEED)
    keys = [records[rng.randrange(n)] for _ in range(50_000)]
    t0 = time.perf_counter()
    found = sum(hash_search(index, k) is not None for k in keys)
    hash_50k = time.perf_counter() - t0
    t0 = time.perf_counter()
    found_binary = sum(binary_search_recursive(sorted_records, k) >= 0 for k in keys)
    binary_50k = time.perf_counter() - t0
    with open("results/challenge_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Reg No: {REG_NO} | Name: P SAI DEEPAK\n")
        f.write(f"Timestamp: {datetime.datetime.now().astimezone().isoformat(timespec='seconds')}\n")
        f.write(f"n={n}; queries=50000; hash_build_seconds={build_s:.6f}; hash_query_seconds={hash_50k:.6f}; binary_50000_seconds={binary_50k:.6f}; hash_found={found}; binary_found={found_binary}\n")
    print("-" * 78)
    print(f"DAY-4 CHALLENGE: n=1,000,000, searches=50,000 | hash build={build_s:.6f}s | hash queries={hash_50k:.6f}s | binary queries={binary_50k:.6f}s | found={found}/{found_binary}")
    print("Wrote results/results.csv and results/challenge_summary.txt")
    print("=" * 78)

if __name__ == "__main__":
    main()
