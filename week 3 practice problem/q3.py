number = int(input("Enter a number: "))
origNumber = number
reversedNumber = 0

while number > 0:
    digit = number % 10
    reversedNumber = reversedNumber * 10 + digit
    number = number // 10

if reversedNumber == origNumber:
    result = True
else:
    result = False

print(f"Is the number {origNumber} a Palindrome? {result}")