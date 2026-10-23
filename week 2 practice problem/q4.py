def mask_phone_number(phone):
    if len(phone) != 10 or not phone.isdigit():
        print("Invalid phone number")
    else:
        masked = "XXXXXX-" + phone[-4:]
        print(masked)


phone = input("Enter phone number: ")
mask_phone_number(phone)