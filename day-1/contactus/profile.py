import uuid
from contact import Contact
from rating import Rate


class User:
    MSG = "MSG"
    RATE = "RATE"

    def __init__(self, username, dob):
        self.uuid = uuid.uuid4()
        self.username = username
        self.dob = dob
        self.messages = []
        self.rates = []

    def send_message(self, reason, description):
        msg = Contact(reason=reason, description=description)
        self.save(msg)
        print("Message Saved")

    def save(self, payload):
        if isinstance(payload, Contact):
            self.messages.append(payload)
        if isinstance(payload, Rate):
            self.rates.append(payload)

    def export_messages_to_txt(self):
        self._export_to_txt(self.messages, User.MSG)

    def export_rates_to_txt(self):
        self._export_to_txt(self.rates, User.RATE)

    def _export_to_txt(self, payload, rate_or_msg):
        with open(f"{self}[{rate_or_msg}].txt", "a") as f:
            for start, msg in enumerate(payload, start=1):
                f.write(f"\n{start}-{msg}\n" + "#" * 30 + "\n")

    def showlogs(self):
        for start, msg in enumerate(self.messages, start=1):
            print(start, msg)

    def __repr__(self):
        return f"[{self.uuid}][{self.username}][{self.dob}]"

    def rateus(self, is_excellent, is_recommended, feedback):
        rate = Rate(is_excellent, is_recommended, feedback)
        self.save(rate)
