class BookInventory:
    def __init__(self, title, author, copiesAvailable):
        self.title = title
        self.author = author
        self.copiesAvailable = copiesAvailable

    def printEntry(self):
        print(
            f"{self.title} by {self.author} - "
            f"{self.copiesAvailable} copies available"
        )


books = [
    BookInventory("Clean Code", "Robert C. Martin", 3),
    BookInventory("Effective Java", "Joshua Bloch", 5),
    BookInventory("Refactoring", "Martin Fowler", 0),
    BookInventory("Design Patterns", "GoF", 2)
]

for book in books:
    book.printEntry()