class IdCard:
    def __init__(self, name, booksIssued):
        self.name = name
        self.booksIssued = booksIssued


ravi = IdCard("Ravi", 0)
duplicate = ravi

duplicate.booksIssued = 3

print(f"Ravi's booksIssued (via first variable): {ravi.booksIssued}")
print(f"duplicate == ravi: {duplicate is ravi}")

separate = IdCard("Ravi", 3)
print(f"separate == ravi: {separate is ravi}")