rows = int(input("Enter the number of rows: "))

print(f"The right-angled triangle pattern for {rows} rows is")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()