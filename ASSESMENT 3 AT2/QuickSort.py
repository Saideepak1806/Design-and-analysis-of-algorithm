print("Name: PINDIBOINA SAI DEEPAK")
print("Register Number: 192411047")

scores = [42, 17, 63, 8, 55, 29]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = sorted([arr[0], arr[len(arr)//2], arr[-1]])[1]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

print("\nOriginal Scores:", scores)

sorted_scores = quick_sort(scores)

print("Sorted Scores:", sorted_scores)