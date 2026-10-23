def reverse_each_word(sentence):
    words = sentence.split(" ")
    reversed_words = []

    for word in words:
        reverse_word = ""

        for char in word:
            reverse_word = char + reverse_word

        reversed_words.append(reverse_word)

    return " ".join(reversed_words)


sentence = input("Enter a sentence: ")
print(reverse_each_word(sentence))