n = int(input())

temp = n
total = 0
reverse = 0

while temp > 0:
    digit = temp % 10
    total += digit
    reverse = reverse * 10 + digit
    temp //= 10

print("Sum of digits:", total)
print("Reverse:", reverse)