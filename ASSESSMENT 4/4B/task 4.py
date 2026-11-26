# Name: PINDIBOINA SAI DEEPAK
# Register Number: 192411047
# Task 4: Assembly Line Scheduling using DP


def assembly_line(a1, a2, t1, t2, entry, exit_time):
    n = len(a1)

    f1 = [0] * n
    f2 = [0] * n

    parent1 = [0] * n
    parent2 = [0] * n

    f1[0] = entry[0] + a1[0]
    f2[0] = entry[1] + a2[0]

    print("\nSTATION DECISION TRACE")
    print("Station | L1 Stay | L1 Transfer | L1 Choice |"
          " L2 Stay | L2 Transfer | L2 Choice")

    print("1 | Entry | Entry | Start | Entry | Entry | Start")

    for j in range(1, n):

        stay1 = f1[j - 1] + a1[j]
        transfer1 = f2[j - 1] + t2[j - 1] + a1[j]

        if stay1 <= transfer1:
            f1[j] = stay1
            parent1[j] = 1
            choice1 = "Stay"
        else:
            f1[j] = transfer1
            parent1[j] = 2
            choice1 = "Transfer"

        stay2 = f2[j - 1] + a2[j]
        transfer2 = f1[j - 1] + t1[j - 1] + a2[j]

        if stay2 <= transfer2:
            f2[j] = stay2
            parent2[j] = 2
            choice2 = "Stay"
        else:
            f2[j] = transfer2
            parent2[j] = 1
            choice2 = "Transfer"

        print(j + 1, stay1, transfer1, choice1,
              stay2, transfer2, choice2)

    finish1 = f1[-1] + exit_time[0]
    finish2 = f2[-1] + exit_time[1]

    if finish1 <= finish2:
        minimum = finish1
        line = 1
    else:
        minimum = finish2
        line = 2

    route = [0] * n
    route[-1] = line

    for j in range(n - 1, 0, -1):
        if route[j] == 1:
            route[j - 1] = parent1[j]
        else:
            route[j - 1] = parent2[j]

    print("\nDP Line 1:", f1)
    print("DP Line 2:", f2)

    print("\nOPTIMAL ROUTE")

    for j in range(n):
        print("Line", route[j], "Station", j + 1)

    transfers = []

    for j in range(1, n):
        if route[j] != route[j - 1]:
            transfers.append(j + 1)

    print("Transfer points:", transfers)
    print("Minimum production time:", minimum)

    return minimum, route


print("Name: PINDIBOINA SAI DEEPAK")
print("Register Number: 192411047")

a1 = [4, 5, 3, 2]
a2 = [2, 10, 1, 4]

t1 = [7, 4, 5]
t2 = [9, 2, 8]

entry = [10, 12]
exit_time = [18, 7]

print("\n========== BASELINE ==========")
assembly_line(a1, a2, t1, t2, entry, exit_time)

print("\n========== CHANGED TRANSFER TIME ==========")
print("Prediction: Increasing the first transfer time")
print("may make transferring before station 2 less attractive.")

changed_t1 = [50, 4, 5]
assembly_line(a1, a2, changed_t1, t2, entry, exit_time)

print("\n========== SLOWER STATION TEST ==========")
print("Prediction: Slowing Line 1 station 3 may change the route.")

changed_a1 = [4, 5, 23, 2]
assembly_line(changed_a1, a2, t1, t2, entry, exit_time)

print("\nTHREE-LINE EXTENSION")
print("The DP state must store the minimum cost for each of")
print("the three lines at every station. Each line compares")
print("staying with transfers from the other two lines.")
print("A predecessor table is used to reconstruct the route.")