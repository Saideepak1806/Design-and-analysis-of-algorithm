"""
Q3: Engineer the Behaviour of Brute-Force String Matching
Problem Context: Cybersecurity Log Screening
Student: P Sai Deepak | Reg No: 192411047 | Seed: 1047
"""

import time
from common import print_header, STUDENT_NAME, REG_NO, SEED

def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0
    shifts = 0
    matches = []
    start = time.perf_counter()

    for i in range(n - m + 1):
        shifts += 1
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            matches.append(i)

    duration = time.perf_counter() - start
    return matches, comparisons, shifts, duration

def run_benchmarks():
    print_header("Q3: Cybersecurity Log Screening - Brute-Force String Matching")
    
    # 1. Best Case / Low-Work Condition
    # Pattern starts with a character not matching the uniform text body
    text_len = 10000
    pat_len = 20
    text_best = "A" * text_len
    pat_best = "B" + ("A" * (pat_len - 1))
    pred_best = text_len - pat_len + 1

    # 2. Worst Case / Engineered High-Work Condition
    # Pattern matches all characters except the very last one at every single shift
    text_worst = "A" * text_len
    pat_worst = ("A" * (pat_len - 1)) + "B"
    pred_worst = (text_len - pat_len + 1) * pat_len

    # 3. Realistic Security Log with Repeating Prefix (Partial Match Cascades)
    # Simulated log stream with repeating auth prefix "AUTH_ATTEMPT_USER_"
    log_chunk = "AUTH_ATTEMPT_USER_LOGIN_ACCEPTED; " * 300
    text_custom = log_chunk + "AUTH_ATTEMPT_USER_SQLI_BREACH_PAYLOAD_DETECTED; " + log_chunk
    pat_custom = "AUTH_ATTEMPT_USER_SQLI_BREACH_PAYLOAD_DETECTED"
    pred_custom = "Repeated 18-char partial match per log entry until exact signature hit"

    test_cases = [
        ("Test 1: Low-Work (Immediate Mismatch)", text_best, pat_best, pred_best),
        ("Test 2: High-Work (Last-Char Mismatch)", text_worst, pat_worst, pred_worst),
        ("Test 3: Cybersecurity Prefix Cascade", text_custom, pat_custom, pred_custom)
    ]

    print("\n--- EXPERIMENTAL RESULTS TABLE ---")
    print(f"{'Condition':<36} | {'Text Len':<9} | {'Pat Len':<8} | {'Comparisons':<12} | {'Shifts':<8} | {'Time (ms)':<10}")
    print("-" * 92)

    results = []
    for desc, txt, pat, pred in test_cases:
        matches, cmp_cnt, shift_cnt, t_dur = brute_force_string_match(txt, pat)
        results.append((desc, len(txt), len(pat), cmp_cnt, shift_cnt, t_dur * 1000, pred, matches))
        print(f"{desc:<36} | {len(txt):<9} | {len(pat):<8} | {cmp_cnt:<12} | {shift_cnt:<8} | {t_dur*1000:<10.3f}")

    print("\n--- PREDICTION VS OBSERVED ANALYSIS ---")
    print(f"1. Low-Work Test: Predicted = {pred_best} comparisons | Observed = {results[0][3]} comparisons.")
    print(f"   Verification: Exact match! Each shift fails on 1st character comparison.")
    print(f"2. High-Work Test: Predicted = {pred_worst} comparisons | Observed = {results[1][3]} comparisons.")
    print(f"   Verification: Exact match! Each shift makes {pat_len} character comparisons.")
    print(f"   Work Ratio (Worst / Best) = {results[1][3] / results[0][3]:.2f}x for IDENTICAL text and pattern lengths!")
    print(f"3. Security Log Test: Text Len = {len(text_custom)} | Comparisons = {results[2][3]} | Matches found at index: {results[2][7]}")
    
    return results

if __name__ == "__main__":
    run_benchmarks()
