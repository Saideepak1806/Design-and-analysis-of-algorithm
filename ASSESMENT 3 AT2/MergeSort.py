print("Name: PINDIBOINA SAI DEEPAK")
print("Register Number: 192411047")

orders = [
    (105, "O1"), (102, "O2"), (105, "O3"),
    (101, "O4"), (102, "O5"), (103, "O6")
]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

sorted_orders = merge_sort(orders)

print("\nSorted Orders:")
for order in sorted_orders:
    print(order[0], "-", order[1])