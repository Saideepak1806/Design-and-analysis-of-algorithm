def linear_search(records, key, counter=None):
    """Return index of key, or -1. records may be any sequence."""
    comparisons = 0
    for i, value in enumerate(records):
        comparisons += 1
        if value == key:
            if counter is not None:
                counter["comparisons"] = counter.get("comparisons", 0) + comparisons
            return i
    if counter is not None:
        counter["comparisons"] = counter.get("comparisons", 0) + comparisons
    return -1
