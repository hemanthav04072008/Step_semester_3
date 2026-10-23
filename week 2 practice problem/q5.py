def normalize_reference(raw):
    reference = raw.strip()

    if len(reference) >= 3:
        reference = reference[:3].upper() + reference[3:]

    return reference


def validate_and_format(reference):
    if len(reference) != 14:
        return "Invalid: wrong length"

    for ch in reference[:3]:
        if not ch.isalpha():
            return "Invalid: bank code must be 3 letters"

    for ch in reference[3:]:
        if not ch.isdigit():
            return "Invalid: body must contain only digits"

    date = reference[3:9]
    formatted_date = date[:2] + "/" + date[2:4] + "/" + date[4:6]
    sequence = reference[9:]

    return f"[{reference[:3]}] DATE: {formatted_date} | SEQ: {sequence}"


raw = input("Enter transaction reference: ")
reference = normalize_reference(raw)
print(validate_and_format(reference))