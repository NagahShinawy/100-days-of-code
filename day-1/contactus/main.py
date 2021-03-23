from profile import User


def main():
    john = User(username="John", dob="2002-03-12")
    john.send_message(reason="COMPLAIN", description="I can't display my personal info")
    john.send_message(reason="SUGGEST", description="Adding Vital Signs Profile")
    john.showlogs()


if __name__ == "__main__":
    main()
