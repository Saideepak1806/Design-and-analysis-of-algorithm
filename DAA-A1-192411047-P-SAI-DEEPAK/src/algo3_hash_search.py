def build_hash_index(records):
    """Build a hash set index. Expected O(n) build time and O(n) extra space."""
    return set(records)

def hash_search(index, key):
    """Return key if present, otherwise None. Expected O(1) lookup."""
    return key if key in index else None
