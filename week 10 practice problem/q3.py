numbers_text = input().strip()
numbers_text = numbers_text.strip("[]")
numbers = list(map(int, numbers_text.replace(",", " ").split()))

even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)