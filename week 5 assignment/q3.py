def find_min_max_spread(scores):
    minimum = scores[0]
    maximum = scores[0]

    for score in scores[1:]:
        if score < minimum:
            minimum = score

        if score > maximum:
            maximum = score

    spread = maximum - minimum

    return f"Min: {minimum} | Max: {maximum} | Spread: {spread}"


scores = [45, 82, 79, 90, 33, 90, 61]

print(find_min_max_spread(scores))