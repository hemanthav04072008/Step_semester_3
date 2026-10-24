import sys

words = sys.stdin.read().split()

for word in words:
    reversed_word = word[::-1]

    if word == reversed_word:
        print(f"{reversed_word} - palindrome")
    else:
        print(f"{reversed_word} - not a palindrome")