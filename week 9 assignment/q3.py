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


item_types = {
    "BOOK": Book,
    "DVD": DVD,
    "MAGAZINE": Magazine
}

n = int(input())
total_fines = 0.0

for _ in range(n):
    item_type, title, days_late = input().split()

    item = item_types[item_type](title, int(days_late))
    fine = item.calculate_fine()

    print(f"{item.title}: {fine:.2f}")
    total_fines += fine

print(f"Total Fines: {total_fines:.2f}")