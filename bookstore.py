class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"{self.book_id} | {self.title} | {self.author} | ${self.price}")


class BookStore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!\n")

    def view_books(self):
        if not self.books:
            print("No books available.\n")
            return

        print("\n----- Book List -----")
        for book in self.books:
            book.display()
        print()

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("\nBook Found:")
                book.display()
                return
        print("Book not found.\n")


# -------- Main Program ---------

store = BookStore()

while True:
    print("===== Book Store =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = int(input("Book ID: "))
        title = input("Title: ")
        author = input("Author: ")
        price = float(input("Price: "))

        book = Book(book_id, title, author, price)
        store.add_book(book)

    elif choice == "2":
        store.view_books()

    elif choice == "3":
        title = input("Enter book title: ")
        store.search_book(title)

    elif choice == "4":
        print("Thank you for using Book Store!")
        break

    else:
        print("Invalid choice.\n")