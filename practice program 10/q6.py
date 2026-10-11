n = int(input())
prime = True

if n <= 1:
    prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break

if prime:
    print(n, "is prime")
else:
    print(n, "is not prime")