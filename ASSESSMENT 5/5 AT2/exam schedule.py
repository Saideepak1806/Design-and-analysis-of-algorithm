
courses = {
    "C1": ("Design and Analysis of Algorithms", 120),
    "C2": ("Operating Systems", 90),
    "C3": ("Database Management Systems", 110),
    "C4": ("Computer Networks", 60),
    "C5": ("Java Programming", 150),
    "C6": ("Discrete Mathematics", 80),
    "C7": ("Artificial Intelligence", 40),
    "C8": ("Cloud Computing", 70)
}

clash_pairs = [
    ("C1", "C2"), ("C1", "C3"), ("C2", "C3"),
    ("C1", "C5"), ("C3", "C5"), ("C2", "C4"),
    ("C4", "C6"), ("C5", "C6"), ("C6", "C7"),
    ("C7", "C8"), ("C3", "C8"), ("C5", "C8"),
    ("C1", "C6")
]

clashes = {frozenset(pair) for pair in clash_pairs}

slots = ["S1", "S2", "S3", "S4"]
halls = {"A": 160, "B": 120}

# Most constrained courses are scheduled first
order = ["C5", "C1", "C3", "C6",
         "C2", "C8", "C4", "C7"]

assigned = {}
occupied = {(s, h): None for s in slots for h in halls}

best_penalty = float("inf")
best_schedule = None
search_nodes = 0


def backtrack(index, penalty):
    global best_penalty, best_schedule, search_nodes

    search_nodes += 1

    # Branch-and-bound pruning
    if penalty >= best_penalty:
        return

    # All courses have been assigned
    if index == len(order):
        best_penalty = penalty
        best_schedule = assigned.copy()
        return

    course = order[index]
    students = courses[course][1]

    for slot in slots:

        # Check clash constraint
        clash_found = False

        for other, (other_slot, other_hall) in assigned.items():
            if (frozenset((course, other)) in clashes
                    and slot == other_slot):
                clash_found = True
                break

        if clash_found:
            continue

        for hall, capacity in halls.items():

            # Check hall capacity and availability
            if students > capacity:
                continue

            if occupied[(slot, hall)] is not None:
                continue

            # Calculate additional same-day clash penalty
            added_penalty = 0

            for other, (other_slot, other_hall) in assigned.items():
                same_day = (
                    (slot in ["S1", "S2"])
                    == (other_slot in ["S1", "S2"])
                )

                if (frozenset((course, other)) in clashes
                        and same_day):
                    added_penalty += 1

            # Make assignment
            assigned[course] = (slot, hall)
            occupied[(slot, hall)] = course

            backtrack(index + 1, penalty + added_penalty)

            # Undo assignment
            occupied[(slot, hall)] = None
            del assigned[course]


# Run the optimisation
backtrack(0, 0)

print("OPTIMISED EXAMINATION TIMETABLE")
print("--------------------------------")

if best_schedule is None:
    print("No feasible timetable found.")
else:
    for slot in slots:
        print("\n", slot)

        for hall in halls:
            course = next(
                (c for c, value in best_schedule.items()
                 if value == (slot, hall)),
                None
            )

            if course:
                name, students = courses[course]
                print(
                    f"Hall {hall}: {course} - {name} "
                    f"({students} students)"
                )

    print("\nMinimum same-day clash penalty:",
          best_penalty)

print("Search nodes explored:", search_nodes)
