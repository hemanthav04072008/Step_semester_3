def normalize_code(raw):
    code = raw.strip()

    if len(code) >= 3:
        code = code[:3].upper() + code[3:]

    return code


def validate_and_format(code):
    if len(code) != 13:
        return "Invalid: code must be exactly 13 characters"

    for char in code[:3]:
        if not char.isalpha():
            return "Invalid: publisher code must be 3 letters"

    for char in code[3:]:
        if not char.isdigit():
            return "Invalid: body must contain only digits"

    year = code[3:7]
    catalog = code[7:13]

    return f"[{code[:3]}] YEAR: {year} | CATALOG: {catalog}"


raw = input("Enter ISBN-style code: ")
normalized = normalize_code(raw)
print(validate_and_format(normalized))