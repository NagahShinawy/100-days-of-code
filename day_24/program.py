"""
created by Nagaj at 10/06/2021
"""
import os

LETTER_PATH = "./inputs/letters/starting_letter.txt"
NAMES_PATH = "./inputs/names/names.txt"
SENDING_MAIL_PATH = "./output/readyToSend"
NOTIFICATION = "MAIL SENT TO '{name}'"


def read_letter() -> str:
    """
    get template body mail to sent to everyone
    :return: string of mail body template read from file
    """
    with open(LETTER_PATH) as fin:
        return fin.read()


def get_names() -> list:
    """
    get list of names in the file to send mail to everyone of them
    :return: list of names
    """
    with open(NAMES_PATH) as fin:
        return [name.strip() for name in fin.readlines()]


def send_mail(names: list, body: str) -> None:
    """
    sending mail to everyone in the names list
    :param names: list of names
    :param body: mail template body
    :return: None
    """
    for name in names:
        mailpath = os.path.join(SENDING_MAIL_PATH, f"letter_for_{name}.txt")
        with open(mailpath, "w") as fout:
            fout.write(body.replace("[name]", name))
        print(NOTIFICATION.format(name=name))


def main():
    """
    entry point for the program
    :return: None
    """
    mail_body = read_letter()
    names = get_names()
    send_mail(names, mail_body)


if __name__ == "__main__":
    main()
