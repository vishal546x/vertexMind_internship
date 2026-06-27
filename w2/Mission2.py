class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def display(self):
        return f"ID: {self.item_id} | Title: {self.title}"

class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def display(self):
        return f"[Book] {super().display()} | Author: {self.author}"

class LibraryManager:
    def __init__(self):
        self.catalog = {}

    def add_item(self, item):
        self.catalog[item.item_id] = item
        print(f"Added: {item.title}")

    def show_catalog(self):
        if not self.catalog:
            print("Catalog is empty.")
        for item in self.catalog.values():
            print(item.display())

def main():
    manager = LibraryManager()
    
    manager.add_item(Book("The Great Gatsby", 101, "F. Scott Fitzgerald"))
    manager.add_item(Book("1984", 102, "George Orwell"))

    print("\n--- Current Catalog ---")
    manager.show_catalog()

    print("\n--- Add a New Book ---")
    try:
        title = input("Enter book title: ")
        item_id = int(input("Enter book numeric ID: "))
        author = input("Enter author: ")
        
        new_book = Book(title, item_id, author)
        manager.add_item(new_book)
        
    except ValueError:
        print("Error: Item ID must be a number! Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()