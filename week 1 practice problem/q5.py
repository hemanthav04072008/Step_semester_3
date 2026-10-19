def reverseCustomerName(customerName):
    return customerName[::-1]


customerName = input("Enter customer name: ")

reversedName = reverseCustomerName(customerName)

print("Original Name:", customerName)
print("Reversed Name:", reversedName)