def parse_student_record(csv_line):
    fields = csv_line.split(",")

    if len(fields) != 3:
        print("Invalid Record")
    else:
        print(
            f"Name: {fields[0]} | "
            f"Roll No: {fields[1]} | Dept: {fields[2]}"
        )


csv_line = input("Enter student record: ")
parse_student_record(csv_line)