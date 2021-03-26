from book import Book
from author import Author


def main():
    clean_code = Book("Clean Code", 12.4)
    python = Book("Python Code", 12.4)
    boob = Author("Boob", 23)
    john = Author("John", 5)
    boob.write(clean_code)
    boob.write(python)
    john.write(python)

    print(clean_code.authors)
    print(python.authors)

    ####################################
    print(john.books)
    print(boob.books)


if __name__ == "__main__":
    main()
