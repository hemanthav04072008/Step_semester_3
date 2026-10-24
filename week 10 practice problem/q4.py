numbers_text = input().strip().strip("[]")
numbers = list(map(int, numbers_text.replace(",", " ").split()))

left = 0
right = len(numbers) - 1

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    left += 1
    right -= 1

print(numbers)