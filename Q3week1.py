number = int (input("Enter the number"))
orgnumber = number 
reversednumber =0
while(number !=0):
    digit = number %10
    reversednumber =reversednumber *10 + digit
    number = number //10
if reversednumber==orgnumber:
    print(orgnumber,'is a palidrome number ')
else:
    print(orgnumber,'is not a palindrome number ')