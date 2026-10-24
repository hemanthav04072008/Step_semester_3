from datetime import date, timedelta
import shlex


class LibraryItem:
    borrowing_days = 0

    def __init__(self, title):
        self.title = title

    def calculate_due_date(self, current_date):
        return current_date + timedelta(days=self.borrowing_days)


class Book(LibraryItem):
    borrowing_days = 14


class DVD(LibraryItem):
    borrowing_days = 7


class Magazine(LibraryItem):
    borrowing_days = 3


ITEM_TYPES = {
    "BOOK": Book,
    "DVD": DVD,
    "MAGAZINE": Magazine
}

current_date = date(2023, 10, 26)
n = int(input())

for _ in range(n):
    parts = shlex.split(input())
    item_type = parts[0]
    title = " ".join(parts[1:])

    item = ITEM_TYPES[item_type](title)
    due_date = item.calculate_due_date(current_date)

    print(f"{item.title}: {due_date}")