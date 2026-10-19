def checkTypingAccuracy(original, typed):
    matched = 0
    firstMismatch = -1

    for i in range(len(original)):
        if original[i] == typed[i]:
            matched += 1
        elif firstMismatch == -1:
            firstMismatch = i

    accuracy = (matched / len(original)) * 100 if original else 100

    print("Matched:", str(matched) + "/" + str(len(original)))
    print("Accuracy: {:.2f}%".format(accuracy))

    if firstMismatch == -1:
        print("No Mismatches")
    else:
        print("First Mismatch at position", firstMismatch + 1,
              "('" + original[firstMismatch] + "' vs '" +
              typed[firstMismatch] + "')")


original = input("Enter original passage: ")
typed = input("Enter typed text: ")

if len(original) == len(typed):
    checkTypingAccuracy(original, typed)
else:
    print("Both strings must have equal length.")