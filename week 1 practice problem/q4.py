def findFirstNonRepeatingChar(text):
    frequency = {}

    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in text:
        if frequency[ch] == 1:
            return ch

    return None


text = input("Enter a word or sentence: ")

result = findFirstNonRepeatingChar(text)

if result is not None:
    print("First Non-Repeating Character:", result)
else:
    print("No Non-Repeating Character Found")