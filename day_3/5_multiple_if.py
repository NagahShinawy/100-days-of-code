def get_ticket():
    total = 0

    ticket = int(input("what is ticket type: 12, 15, 17, 20"))

    wants_photo = input("Want photo ?Y/N")

    want_horse = input("Want horse ridY/N:")

    if wants_photo == "Y":
        ticket += 5

    if want_horse == "Y":
        ticket += 7


def total_bill():
    height = int(input("Enter Height"))
    if height >= 120:
        age = int(input("Enter Age"))
        if age < 12:
            bill = 5

        elif age <= 18:
            bill = 7
        else:
            bill = 12
        wants_photo = input("Want Photo Y / N")

        wants_horse = input("Wants Horse Y/ N")
        if wants_photo == "Y":
            bill += 3
        if wants_horse == "Y":
            bill += 4
        print("Total Bill is", bill)
    else:
        print("Just Only 120 CM or longer")


# print("Ticket is ", get_ticket())

total_bill()
