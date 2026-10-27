"""
Q1: Sorting Under Different Data Conditions
Problem Context: E-Commerce Order Processing (Dispatch Priority Scores)
Algorithms: Selection Sort, Bubble Sort (with early exit), Insertion Sort
Student: P Sai Deepak | Reg No: 192411047 | Seed: 1047
"""

import time
import random
import sys
import os

from common import print_header, set_seed, STUDENT_NAME, REG_NO, SEED

def selection_sort(arr):
    a = list(arr)
    n = len(a)
    comparisons = 0
    swaps = 0
    start = time.perf_counter()
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    duration = time.perf_counter() - start
    return a, comparisons, swaps, duration

def bubble_sort(arr):
    a = list(arr)
    n = len(a)
    comparisons = 0
    swaps = 0
    start = time.perf_counter()
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    duration = time.perf_counter() - start
    return a, comparisons, swaps, duration

def insertion_sort(arr):
    a = list(arr)
    n = len(a)
    comparisons = 0
    shifts = 0
    start = time.perf_counter()
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key
    duration = time.perf_counter() - start
    return a, comparisons, shifts, duration

def generate_datasets(n):
    set_seed()
    # 1. Randomly ordered (Contrasting Dataset 1)
    random_data = [random.randint(100, 9999) for _ in range(n)]
    
    # 2. Significantly disordered / Reverse sorted (Contrasting Dataset 2)
    reverse_data = sorted(random_data, reverse=True)
    
    # 3. 95% Nearly Sorted (Edge-Case Dataset 3: e-commerce batch arrival)
    nearly_sorted = sorted(random_data)
    num_disordered = max(1, int(0.05 * n))
    for _ in range(num_disordered):
        idx1 = random.randint(0, n - 1)
        idx2 = random.randint(0, n - 1)
        nearly_sorted[idx1], nearly_sorted[idx2] = nearly_sorted[idx2], nearly_sorted[idx1]
        
    return {
        "Random": random_data,
        "Reverse Sorted": reverse_data,
        "95% Nearly Sorted": nearly_sorted
    }

def run_benchmarks():
    print_header("Q1: E-Commerce Dispatch Priority Sorting Investigation")
    test_sizes = [500, 1000, 2000, 3000]
    records = []

    print("\n--- EXPERIMENTAL RESULTS TABLE ---")
    print(f"{'Condition':<18} | {'N':<5} | {'Algorithm':<14} | {'Comparisons':<12} | {'Swaps/Moves':<12} | {'Time (ms)':<10}")
    print("-" * 84)

    for n in test_sizes:
        datasets = generate_datasets(n)
        for cond_name, data in datasets.items():
            # Selection Sort
            _, s_cmp, s_swp, s_t = selection_sort(data)
            records.append(("Selection Sort", cond_name, n, s_cmp, s_swp, s_t * 1000))
            print(f"{cond_name:<18} | {n:<5} | {'Selection':<14} | {s_cmp:<12} | {s_swp:<12} | {s_t*1000:<10.3f}")

            # Bubble Sort
            _, b_cmp, b_swp, b_t = bubble_sort(data)
            records.append(("Bubble Sort", cond_name, n, b_cmp, b_swp, b_t * 1000))
            print(f"{cond_name:<18} | {n:<5} | {'Bubble':<14} | {b_cmp:<12} | {b_swp:<12} | {b_t*1000:<10.3f}")

            # Insertion Sort
            _, i_cmp, i_swp, i_t = insertion_sort(data)
            records.append(("Insertion Sort", cond_name, n, i_cmp, i_swp, i_t * 1000))
            print(f"{cond_name:<18} | {n:<5} | {'Insertion':<14} | {i_cmp:<12} | {i_swp:<12} | {i_t*1000:<10.3f}")
            print("-" * 84)

    return records

if __name__ == "__main__":
    run_benchmarks()
