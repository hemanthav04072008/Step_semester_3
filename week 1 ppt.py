a=int(input("Enter the number"))
isprime = True
for i in range (2,a):
    if (a%i==0):
        isprime =False
        break
if isprime :
    print(a,"is a prime number")
else:
    print(a,"is not a prime number ")
