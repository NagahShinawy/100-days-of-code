import uuid
from contact import Contact


class User:
    def __init__(self, username, dob):
        self.uuid = uuid.uuid4()
        self.username = username
        self.dob = dob
        self.messages = []

    def send_message(self, reason, description):
        msg = Contact(reason=reason, description=description)
        self.save(msg)
        print("Message Saved")

    def save(self, msg):
        self.messages.append(msg)

    def export_to_txt(self):
        with open(f"[{self.uuid}][{self.username}][{self.dob}].txt", "w") as f:
            for start, msg in enumerate(self.messages, start=1):
                f.write(f"{start}-{msg}\n")

    def showlogs(self):
        for start, msg in enumerate(self.messages, start=1):
            print(start, msg)

    def __repr__(self):
        return self.username + " " + self.dob
