def find_top_three_scores(scores):
    first = float("-inf")
    second = float("-inf")
    third = float("-inf")

    for score in scores:
        if score >= first:
            third = second
            second = first
            first = score
        elif score >= second:
            third = second
            second = score
        elif score >= third:
            third = score

    return [first, second, third]


scores = [45, 82, 79, 90, 33, 90, 61]
print(find_top_three_scores(scores))