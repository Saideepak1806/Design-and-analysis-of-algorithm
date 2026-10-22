def binary_search_recursive(records, key, low=0, high=None, counter=None):
    """Recursive binary search. records must be sorted in ascending order."""
    if high is None:
        high = len(records) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if counter is not None:
        counter["comparisons"] = counter.get("comparisons", 0) + 1
    if records[mid] == key:
        return mid
    if key < records[mid]:
        return binary_search_recursive(records, key, low, mid - 1, counter)
    return binary_search_recursive(records, key, mid + 1, high, counter)
