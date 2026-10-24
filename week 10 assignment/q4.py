def rotateRoster(names, k):
    n = len(names)
    k = k % n

    if k == 0:
        return names.copy()

    return names[-k:] + names[:-k]


print(rotateRoster(["A", "B", "C", "D", "E"], 2))
print(rotateRoster(["A", "B", "C", "D", "E"], 7))