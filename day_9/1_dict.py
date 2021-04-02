errors = {
    "typeerror": "TypeError",
    "valueerror": "ValueError",
    "keyerror": "KeyError",
    "indexerror": "IndexError",
}

clean_code_book = {
    "title": "Clean Code",
    "price": "23$",
    "author": "bob",
    "published": 2012,
    "version": "v.1.3",
}

django_book = {
    "title": "Django Framework",
    "price": "20$",
    "author": "James",
    "published": 2018,
    "version": "2.3",
}

books = [
    clean_code_book,
    django_book,
]

print(clean_code_book)
print(django_book)

print("#" * 30)

print(books[0]["published"])
print(books[1]["published"])

# adding new key-value to dict
clean_code_book.update({"pages": 300})
django_book.update({"pages": 250})

print(clean_code_book)

pycharm = {
    "name": "pycharm",
    "version": "2021.1",
    "is_pro": True,
    "supports": ["python", "django", "flask", "js", "VCS", "debugging"],
}

vscode = {
    "name": "VsCode",
    "version": "2021",
    "is_pro": False,
    "supports": ["js", "python", "php", "web development"],
}

tools_installed = [pycharm, vscode]


print(pycharm["name"])

# pycharm.update({"name": "Pycharm IDE"})
pycharm["name"] = "Pycharm IDE"
print(pycharm["name"])


print("#" * 50)

for tool in tools_installed:
    for key in tool:
        print(f"{key} : {tool[key]}")
    print("*" * 50)
