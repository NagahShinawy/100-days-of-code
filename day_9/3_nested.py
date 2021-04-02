capitals = {"Egypt": "Cairo", "France": "Paris", "German": "Berlin"}

travel_logs = {
    "France": ["Paris", "Leon"],
    "Egypt": ["Cairo", "Alex", "Luxor", "Aswan", "Giza"],
}

DEGREES = ("A", "A+", "B", "B+", "A+", "C", "D")

book = {
    "title": "Clean code",
    "published": 2012,
    "author": {
        "name": "Bob",
        "dob": 1980,
        "job title": "software engineer",
        "experience": "+25",
        "emails": ["bob@test.com", "bob2@test.com"],
        "location": {"country": "England", "city": "London"},
    },
}

print(book["author"]["location"]["city"])
