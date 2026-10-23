number = int(input("Enter a number: "))
isPrime = True

if number < 2:
    isPrime = False
else:
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break

print(f"Is the number {number} a Prime number? {isPrime}")