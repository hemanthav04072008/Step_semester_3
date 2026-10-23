number = int(input("Enter a number: "))
origNumber = number
sum = 0
digits = len(str(number))

while number > 0:
    digit = number % 10
    sum = sum + digit ** digits
    number = number // 10

if sum == origNumber:
    result = True
else:
    result = False

print(f"Is the number {origNumber} an Armstrong number? {result}")