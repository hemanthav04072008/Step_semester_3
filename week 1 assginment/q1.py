def checkDuplicateSeats(seatNumbers):
    found = False

    for i in range(len(seatNumbers)):
        for j in range(i + 1, len(seatNumbers)):
            if seatNumbers[i] == seatNumbers[j]:
                already_printed = False

                for k in range(i):
                    if seatNumbers[k] == seatNumbers[i]:
                        already_printed = True
                        break

                if not already_printed:
                    print("Duplicate Seat Number Found:", seatNumbers[i])
                    found = True

    if not found:
        print("No Duplicate Seats Found")


seatNumbers = list(map(int, input("Enter seat numbers: ").split()))
checkDuplicateSeats(seatNumbers)