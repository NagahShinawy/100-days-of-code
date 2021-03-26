class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
        self.authors = []

    def __repr__(self):
        return f"<{self.title}>"

    def __getitem__(self, item):
        return self.authors[item]
