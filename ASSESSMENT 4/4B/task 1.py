# Name: PINDIBOINA SAI DEEPAK
# Register Number: 192411047
# Task 1: Word Wrap using Dynamic Programming

def word_wrap(words, width):
    n = len(words)

    if any(len(word) > width for word in words):
        print("Invalid input: A word exceeds line width.")
        return

    dp = [float("inf")] * (n + 1)
    choice = [-1] * n
    dp[n] = 0

    for i in range(n - 1, -1, -1):
        used = 0

        for j in range(i, n):
            used += len(words[j]) + (1 if j > i else 0)

            if used > width:
                break

            spaces = width - used
            penalty = 0 if j == n - 1 else spaces ** 3

            cost = penalty + dp[j + 1]

            if cost < dp[i]:
                dp[i] = cost
                choice[i] = j

    print("\nDP STATES")
    for i in range(n + 1):
        print("dp[", i, "] =", dp[i])

    print("\nFINAL WORD ARRANGEMENT")
    i = 0
    line_no = 1

    while i < n:
        j = choice[i]
        line = words[i:j + 1]

        used = sum(len(w) for w in line) + len(line) - 1
        spaces = width - used
        penalty = 0 if j == n - 1 else spaces ** 3

        print("\nLine", line_no, ":", " ".join(line))
        print("Unused spaces:", spaces)
        print("Line penalty:", penalty)

        i = j + 1
        line_no += 1

    print("\nMinimum total penalty:", dp[0])


words = ["Dynamic", "programming", "creates",
         "optimal", "layouts", "for", "documents"]

print("Name: PINDIBOINA SAI DEEPAK")
print("Register Number: 192411047")

for width in [16, 20, 12]:
    print("\n========== LINE WIDTH:", width, "==========")
    word_wrap(words, width)

print("\n========== BOUNDARY TEST ==========")
word_wrap(["Data", "Science"], 11)