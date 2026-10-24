from bisect import bisect_left, bisect_right


def countInBand(scores, low, high):
    left = bisect_left(scores, low)
    right = bisect_right(scores, high)
    return right - left


scores = [35, 42, 42, 50, 58, 58, 58, 63, 71, 88]

print(countInBand(scores, 42, 58))
print(countInBand(scores, 90, 100))