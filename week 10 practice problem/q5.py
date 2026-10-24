number = int(input())

temp = number
digit_sum = 0
reversed_number = 0

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    reversed_number = reversed_number * 10 + digit
    temp //= 10

print("Sum of digits:", digit_sum)
print("Reverse:", reversed_number)