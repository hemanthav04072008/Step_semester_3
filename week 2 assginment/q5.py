import re

def print_filtered_word_frequency(feedback):
    stop_words = {"the", "was", "and", "a", "is", "of", "in"}

    feedback = feedback.lower()
    feedback = feedback.replace(".", "")
    feedback = feedback.replace(",", "")

    words = re.split(r"\s+", feedback.strip())
    frequency = {}

    for word in words:
        if word and word not in stop_words:
            frequency[word] = frequency.get(word, 0) + 1

    sorted_words = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for word, count in sorted_words:
        print(f"{word}: {count}")


feedback = input("Enter feedback: ")
print_filtered_word_frequency(feedback)