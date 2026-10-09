from datetime import date, timedelta


class LibraryItem:
    def __init__(self, title):
        self.title = title

    def get_due_date(self):
        pass


class Book(LibraryItem):
    def get_due_date(self):
        return date(2023, 10, 26) + timedelta(days=14)


class DVD(LibraryItem):
    def get_due_date(self):
        return date(2023, 10, 26) + timedelta(days=7)


class Magazine(LibraryItem):
    def get_due_date(self):
        return date(2023, 10, 26) + timedelta(days=3)


n = int(input())

for i in range(n):
    data = input().split(maxsplit=1)

    item_type = data[0]
    title = data[1].strip('"')

    if item_type == "BOOK":
        item = Book(title)
    elif item_type == "DVD":
        item = DVD(title)
    else:
        item = Magazine(title)

    print(f"{item.title}: {item.get_due_date()}")