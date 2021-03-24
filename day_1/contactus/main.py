from contactus.profile import User


def main():
    john = User(username="John", dob="2002-03-12")
    john.send_message(reason="COMPLAIN", description="I can't display my personal info")
    john.rateus(is_excellent=True, is_recommended=True, feedback="VERY GOOD")
    john.export_messages_to_txt()
    john.export_rates_to_txt()


def notification():
    from win10toast import ToastNotifier

    ToastNotifier().show_toast(
        "Logs", "Logs Saved Please Check it", duration=3,
    )


if __name__ == "__main__":
    main()
    notification()
