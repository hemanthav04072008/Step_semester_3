def isPalindromeIterative(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True


def isPalindromeRecursive(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return isPalindromeRecursive(text[1:-1])


def isPalindromeArrayReversal(text):
    arr = list(text)
    reversed_arr = arr[::-1]
    return arr == reversed_arr


text = input("Enter a word: ")

print("Iterative:", "Palindrome" if isPalindromeIterative(text) else "Not Palindrome")
print("Recursive:", "Palindrome" if isPalindromeRecursive(text) else "Not Palindrome")
print("Array Reversal:", "Palindrome" if isPalindromeArrayReversal(text) else "Not Palindrome")