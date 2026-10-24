class Scorecard:
    def __init__(self, total_questions):
        self.__results = [None] * total_questions
        self.__total_questions = total_questions
        self.__recorded = 0

    def recordAnswer(self, is_correct):
        if self.__recorded < self.__total_questions:
            self.__results[self.__recorded] = is_correct
            self.__recorded += 1
        else:
            print("All answers recorded")

    def getScore(self):
        score = 0

        for i in range(self.__recorded):
            if self.__results[i]:
                score += 1

        return score


sc = Scorecard(4)
sc.recordAnswer(True)
sc.recordAnswer(True)
sc.recordAnswer(False)
sc.recordAnswer(True)

print("Final score =", sc.getScore())