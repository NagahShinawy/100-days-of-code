from contact import Contact


class User:
    def __init__(self, username, dob):
        self.username = username
        self.dob = dob
        self.messages = []

    def send_message(self, reason, description):
        msg = Contact(reason=reason, description=description)
        self.save(msg)
        print("Message Saved")

    def save(self, msg):
        self.messages.append(msg)

    def showlogs(self):
        for start, msg in enumerate(self.messages, start=1):
            print(start, msg)

    def __repr__(self):
        return self.username + " " + self.dob
