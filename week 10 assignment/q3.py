def secondHighest(scores):
    highest = -1
    second = -1

    for score in scores:
        if score > highest:
            second = highest
            highest = score
        elif highest > score > second:
            second = score

    return second


print(secondHighest([45, 78, 92, 78, 60]))
print(secondHighest([50, 50, 50]))