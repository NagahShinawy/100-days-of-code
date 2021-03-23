class Contact:
    REASONS = ["COMPLAIN", "SUGGEST", "INFO"]

    def __init__(self, reason, description):
        self.reason = reason
        self.description = description

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, reason):
        if reason not in self.REASONS:
            raise ValueError(f"Reason should be one of ({','.join(self.REASONS)})")
        self._reason = reason

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if len(description) < 10:
            raise ValueError("Description should be at least 10 chars")
        self._description = description

    def __repr__(self):
        return f"[{self.reason}] - [{self.description}]"


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
        for msg in self.messages:
            print(msg)

    def __repr__(self):
        return self.username + " " + self.dob


if __name__ == "__main__":
    john = User(username="John", dob="2002-03-12")
    john.send_message(reason="COMPLAIN", description="I can't display my personal info")
    john.send_message(reason="SUGGEST", description="Adding Vital Signs Profile")
    john.showlogs()
