class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
        self.authors = []

    def to_json(self):
        return {
            "name": self.title,
            "yoe": self.price,
            "authors": [author.to_json() for author in self.authors],
        }

    def __repr__(self):
        return f"<{self.title}>"

    def __getitem__(self, item):
        return self.authors[item]
