def row_average(row):
    if len(row) == 0:
        return 0

    return sum(row) / len(row)


def classify_rows(seating_scores, threshold):
    result = []

    for i in range(len(seating_scores)):
        average = row_average(seating_scores[i])

        if average < threshold:
            zone = "Quiet Zone"
        else:
            zone = "Buzzing Zone"

        result.append(f"Row {i}: {zone}")

    return " | ".join(result)


seating_scores = [
    [40, 50, 45],
    [85, 90, 95],
    [30, 20, 25]
]

threshold = 60
print(classify_rows(seating_scores, threshold))