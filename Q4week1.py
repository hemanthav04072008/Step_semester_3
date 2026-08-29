number1 = int (input("Enter the first number"))
number2 = int (input("Enter the second number"))
a=number1
b=number2
while(number2 !=0):
    reminder=number1%number2
    number1=number2
    number2=reminder
print("The GCD of ",a,'and',b,'is',number1)
