users = [
    {"username": "leon", "password": "123"},
    {"username": "john", "password": "123"},
    {"username": "leon", "password": "123"},
    {"username": "james", "password": "123"},
    {"username": "sara", "password": "123"},
]


def login(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("login successfully")
            token = "something"
            refresh_token = "something"
            return token, refresh_token
    print("Invalid username or password")


def main():
    tokens = login("leon", "123")

    if tokens is not None:
        access_token = tokens[0]
        refresh_token = tokens[1]
        print(access_token, refresh_token)


if __name__ == "__main__":
    main()
