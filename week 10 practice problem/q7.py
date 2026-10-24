import sys

numbers = list(map(int, sys.stdin.read().split()))

for number in numbers:
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    print(factorial)