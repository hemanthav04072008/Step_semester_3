def count_vowels_and_consonants(text):
    vowels = 0
    consonants = 0

    for ch in text:
        ch = ch.lower()

        if ch in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1

    print("Vowels:", vowels, "| Consonants:", consonants)


text = input("Enter text: ")
count_vowels_and_consonants(text)