import math
import sys

numbers = list(map(int, sys.stdin.read().split()))

for number in numbers:
    is_prime = number > 1

    for divisor in range(2, math.isqrt(number) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")