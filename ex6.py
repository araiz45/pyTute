class Library:
    def __init__(self):
        self.books = []
        self.noBooks = 0
    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)
    def booksInfo(self):
        print(f"the Library has {self.noBooks}")


harry = Library()
harry.addBook("Harry Potter 1")
harry.addBook("Harry Potter 2")
harry.addBook("Harry Potter 3")
harry.addBook("Harry Potter 4")
print(harry.booksInfo())