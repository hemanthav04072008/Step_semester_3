class Scorecard:
    def __init__(self, questions):
        self.__results = [False] * questions
        self.__count = 0
    def recordAnswer(self, result):
        if self.__count < len(self.__results):
            self.__results[self.__count] = result
            self.__count += 1
    def getScore(self):
        score = 0
        for result in self.__results:
            if result:
                score += 1
        return score
sc = Scorecard(4)
sc.recordAnswer(True)
sc.recordAnswer(True)
sc.recordAnswer(False)
sc.recordAnswer(True)
print(sc.getScore())