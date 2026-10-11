def rotateRoster(names, k):
    n = len(names)
    k = k % n

    return names[-k:] + names[:-k] if k != 0 else names[:]


names = ["A", "B", "C", "D", "E"]
print(rotateRoster(names, 2))
print(rotateRoster(names, 7))