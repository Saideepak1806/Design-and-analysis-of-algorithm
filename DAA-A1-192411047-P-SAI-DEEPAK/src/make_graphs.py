import csv
from pathlib import Path
import matplotlib.pyplot as plt

rows = list(csv.DictReader(open("results/results.csv", newline="", encoding="utf-8")))
out = Path("results/graphs"); out.mkdir(parents=True, exist_ok=True)
algs = sorted(set(r["algorithm"] for r in rows))
sizes = sorted(set(int(r["n"]) for r in rows))
for metric, ylabel, title, filename in [
    ("search_seconds_2_queries", "Seconds for two searches", "Measured search time (2 queries)", "search_runtime.png"),
    ("comparisons_2_queries", "Key comparisons", "Key comparisons for two searches", "comparison_counts.png"),
    ("total_seconds", "Seconds including preprocessing", "Total cost including preprocessing", "total_cost.png"),
]:
    plt.figure(figsize=(8,5))
    for alg in algs:
        xs=[]; ys=[]
        for r in rows:
            if r["algorithm"] == alg:
                try: y=float(r[metric])
                except (ValueError, TypeError): continue
                xs.append(int(r["n"])); ys.append(y)
        if xs:
            plt.plot(xs, ys, marker="o", label=alg)
    plt.xscale("log"); plt.yscale("log")
    plt.xlabel("Input size n (log scale)"); plt.ylabel(ylabel); plt.title(title)
    plt.grid(True, which="both", alpha=.3); plt.legend(); plt.tight_layout()
    plt.savefig(out/filename, dpi=160); plt.close()
print(f"Graphs saved to {out}")
