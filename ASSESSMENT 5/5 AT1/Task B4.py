
def next_fit_decreasing(workloads, capacity):

    if any(x < 0 or x > capacity for x in workloads):
        raise ValueError("Invalid workload")

    items = sorted(workloads, reverse=True)

    servers = []
    remaining = []

    for item in items:

        if not servers:
            servers.append([item])
            remaining.append(capacity - item)
            continue

        current = len(servers) - 1

        if remaining[current] >= item:
            servers[current].append(item)
            remaining[current] -= item
        else:
            servers.append([item])
            remaining.append(capacity - item)

    print("\nNumber of servers:", len(servers))

    for i, server in enumerate(servers):
        print("\nServer", i + 1)
        print("Workloads:", server)
        print("Used capacity:", sum(server))
        print("Remaining capacity:", remaining[i])

    return servers


# Normal test
print("NORMAL TEST")
next_fit_decreasing([4, 8, 1, 4, 2, 1], 10)


# Challenging test
print("\nCHALLENGING TEST")
next_fit_decreasing([6, 6, 4, 4, 4, 4], 10)
