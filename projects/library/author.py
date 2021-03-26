from book import Book


class Author:
    def __init__(self, name, yoe):
        self.name = name
        self.yoe = yoe
        self.books = []

    def write(self, book: Book):
        self.books.append(book)
        book.authors.append(self)

    def to_json(self):
        return {
            "name": self.name,
            "yoe": self.yoe,
            "books": [book.to_json() for book in self.books],
        }

    def __repr__(self):
        return f"<{self.name}>"
