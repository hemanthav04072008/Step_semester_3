def validate_file_extension(filename):
    dot = filename.rfind(".")

    if dot != -1:
        extension = filename[dot + 1:]

        if extension.lower() in ["pdf", "docx", "zip"]:
            return "Accepted"

    return "Rejected — invalid file type"


filename = input("Enter filename: ")
print(validate_file_extension(filename))