"""
created by Nagaj at 10/06/2021
"""
import os


LETTER_PATH = "./inputs/letters/starting_letter.txt"
NAMES_PATH = "./inputs/names/names.txt"
SENDING_MAIL_PATH = "./output/readyToSend"
NOTIFICATION = "MAIL SENT TO '{name}'"


class File:
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return f"File <{self.path}>"

    def __getitem__(self, item):
        return self.lines[item]

    @property
    def content(self):
        with open(self.path, "r") as fin:
            return fin.read()

    @property
    def lines(self):
        with open(self.path) as fin:
            return [name.strip() for name in fin.readlines()]

    def write(self, content):
        with open(self.path, "w") as fout:
            fout.write(content)


class Mail:
    def __init__(self, recipient, content, saved_to):
        self.recipient = recipient
        self.content = content
        self.saved_to = saved_to

    def send(self):
        mailpath = os.path.join(self.saved_to, f"letter_for_{self.recipient}.txt")
        with open(mailpath, "w") as fout:
            fout.write(self.content)
        print(NOTIFICATION.format(name=self.recipient))


if __name__ == "__main__":
    namef = File(path=NAMES_PATH)
    mailtemplate = File(path=LETTER_PATH).content

    for name in namef:
        body = mailtemplate.replace("[name]", name)
        new_main = Mail(recipient=name, content=body, saved_to=SENDING_MAIL_PATH)
        new_main.send()
