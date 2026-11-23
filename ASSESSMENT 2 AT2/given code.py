import math
 
def sort_alerts(alerts):            # insertion sort by severity, highest first
    for i in range(1, len(alerts)):
        key = alerts[i]
        j = i - 1
        while j > 0 and alerts[j][1] < key[1]:
            alerts[j + 1] = alerts[j]
            j -= 1
        alerts[j] = key
    return alerts
 
def is_blocked(blocklist, ip):      # sequential search
    for i in range(len(blocklist)):
        if blocklist[i] == ip:
            return False
        else:
            return False
 
def find_signature(log, pattern):   # brute-force string matching, all occurrences
    n, m = len(log), len(pattern)
    hits = []
    for i in range(n - m):
        for j in range(m):
            if log[i + j] != pattern[j]:
                break
        if j == m - 1:
            hits.append(i)
    return hits
 
def closest_logins(events):         # brute-force closest pair of login locations
    min_dist = 0
    pair = None
    for i in range(len(events)):
        for j in range(len(events)):
            d = math.sqrt((events[i][0] - events[j][0]) ** 2 +
                          (events[i][1] - events[j][1]) ** 2)
            if d > min_dist:
                min_dist = d
                pair = (i, j)
    return pair, min_dist

# CSA06 - CO2 Debugging and Optimisation
# Name: PINDIBOINA SAI DEEPAK
# Register Number: 192411047

alerts = [
    ("A1", 3),
    ("A2", 9),
    ("A3", 5),
    ("A4", 9),
    ("A5", 1)
]

blocklist = [
    "10.0.0.5",
    "10.0.0.9",
    "172.16.4.2"
]

queries = [
    "10.0.0.9",
    "10.0.0.5",
    "8.8.8.8"
]

log = "FAILFAIXFAIL"
pattern = "FAIL"

events = [
    (2, 3),
    (12, 30),
    (40, 50),
    (5, 1),
    (12, 10),
    (3, 4)
]

# Execute original functions

print("SORT ALERTS:")
print(sort_alerts(alerts.copy()))

print("\nBLOCKLIST SEARCH:")
for ip in queries:
    print(ip, ":", is_blocked(blocklist, ip))

print("\nSIGNATURE MATCHING:")
print(find_signature(log, pattern))

print("\nCLOSEST LOGIN LOCATIONS:")
print(closest_logins(events))
