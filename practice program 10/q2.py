class Word:
    def __init__(self, name):
        self.name = name

    def check(self):
        chars = list(self.name)
        chars.reverse()
        reversed_word = "".join(chars)

        if self.name == reversed_word:
            print(reversed_word, "- palindrome")
        else:
            print(reversed_word, "- not a palindrome")


word = input()
obj = Word(word)
obj.check()