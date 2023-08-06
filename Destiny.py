class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                break

    def search_book(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        return found_books

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False
                return True
        return False

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and not book.available:
                book.available = True
                return True
        return False

def main():
    library = Library()
    library.add_book(1, "Book 1", "Author 1")
    library.add_book(2, "Book 2", "Author 2")
    library.add_book(3, "Book 3", "Author 3")

    print("Welcome to the Library Management System!")
    while True:
        print("\n1. Search Book\n2. Borrow Book\n3. Return Book\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter the title of the book you want to search: ")
            found_books = library.search_book(title)
            if found_books:
                print("Found Books:")
                for book in found_books:
                    print(f"{book.book_id}. {book.title} by {book.author}")
            else:
                print("No books found with that title.")

        elif choice == 2:
            book_id = int(input("Enter the book ID you want to borrow: "))
            if library.borrow_book(book_id):
                print("Book successfully borrowed.")
            else:
                print("Book not available or does not exist.")

        elif choice == 3:
            book_id = int(input("Enter the book ID you want to return: "))
            if library.return_book(book_id):
                print("Book successfully returned.")
            else:
                print("Book not borrowed or does not exist.")

        elif choice == 4:
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()