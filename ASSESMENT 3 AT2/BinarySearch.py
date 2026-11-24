print("Name: PINDIBOINA SAI DEEPAK")
print("Register Number: 192411047")

timestamps = [101, 102, 102, 103, 105, 105]
target = 102

def first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

position = first_occurrence(timestamps, target)

if position != -1:
    print("\nFirst occurrence of", target, "is at index", position)
else:
    print("\nTimestamp not found")