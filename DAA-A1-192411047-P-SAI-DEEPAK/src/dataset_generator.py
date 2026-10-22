import random
import csv
from pathlib import Path

REG_NO = "192411047"
SEED = int(REG_NO[-4:])

def generate_records(n, seed=SEED):
    """Generate deterministic, unique registration-number-like integers."""
    rng = random.Random(seed + n)
    # Distinct integer IDs, shuffled to make linear search non-ordered.
    records = list(range(100000000, 100000000 + n))
    rng.shuffle(records)
    # Personal found key is always included; this value is in the ID range.
    personal_key = int(REG_NO)
    if personal_key not in records:
        records[0] = personal_key
    return records

def write_sample(path="data/sample_1000.csv", n=1000):
    records = generate_records(n)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["registration_number"])
        w.writerows([[x] for x in records])
    return path

if __name__ == "__main__":
    print(f"Reg No: {REG_NO} | Name: P SAI DEEPAK")
    print(f"Generated sample: {write_sample()}")
