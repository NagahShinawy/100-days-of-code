from book import Book


class Author:
    def __init__(self, name, yoe):
        self.name = name
        self.yoe = yoe
        self.books = []

    def write(self, book: Book):
        self.books.append(book)
        book.authors.append(self)

    def __repr__(self):
        return f"<{self.name}>"
