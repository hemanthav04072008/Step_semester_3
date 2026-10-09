from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, days_late):
        self.title = title
        self.days_late = days_late

    @abstractmethod
    def calculate_fine(self):
        pass

class Book(LibraryItem):
    def calculate_fine(self):
        return self.days_late * 2

class DVD(LibraryItem):
    def calculate_fine(self):
        return min(self.days_late * 5, 50)

class Magazine(LibraryItem):
    def calculate_fine(self):
        return self.days_late * 1

n = int(input())
items = []

for _ in range(n):
    data = input().split()
    item_type = data[0]
    title = data[1]
    days = int(data[2])

    if item_type == "BOOK":
        items.append(Book(title, days))
    elif item_type == "DVD":
        items.append(DVD(title, days))
    elif item_type == "MAGAZINE":
        items.append(Magazine(title, days))

total = 0

for item in items:
    fine = item.calculate_fine()
    print(f"{item.title}: {fine:.2f}")
    total += fine

print(f"Total Fines: {total:.2f}")