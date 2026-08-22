number=int(input("Enter the number"))
orgnumber=number
sum=0
while(number!=0):
    digit=number%10
    sum=sum+digit**3
    number=number//10
if sum==orgnumber:
    print(orgnumber,'is an armstrong number')
else:
    print(orgnumber,'is not an armstrong number')