def findLongestStreak(signalLog):
    if not signalLog:
        print("Signal log is empty")
        return

    maxCount = 1
    currentCount = 1
    maxColor = signalLog[0]

    for i in range(1, len(signalLog)):
        if signalLog[i] == signalLog[i - 1]:
            currentCount += 1
        else:
            currentCount = 1

        if currentCount > maxCount:
            maxCount = currentCount
            maxColor = signalLog[i]

    print("Longest Streak: '" + maxColor +
          "' repeated", maxCount, "times")


signalLog = input("Enter signal log: ").upper()
findLongestStreak(signalLog)