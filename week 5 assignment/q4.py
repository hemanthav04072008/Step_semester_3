def row_average(row):
    if len(row) == 0:
        return 0.0

    return sum(row) / len(row)


def classify_matches(runs_per_over, threshold):
    result = []

    for i in range(len(runs_per_over)):
        average = row_average(runs_per_over[i])

        if average >= threshold:
            status = "Power Surge"
        else:
            status = "Normal"

        result.append(f"Match {i}: {status}")

    return " | ".join(result)


runs_per_over = [
    [4, 6, 8],
    [10, 12, 14],
    [2, 3, 1]
]

threshold = 8

print(classify_matches(runs_per_over, threshold))