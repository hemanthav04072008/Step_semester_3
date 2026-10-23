def curve_scores(scores, bonus):
    for i in range(len(scores)):
        scores[i] += bonus


scores = [70, 85, 60]
curve_scores(scores, 10)
print(scores)