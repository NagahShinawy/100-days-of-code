def total_bill():
    height = int(input("Enter Height"))
    if height >= 120:
        age = int(input("Enter Age"))
        if age < 12:
            bill = 5

        elif age <= 18:
            bill = 7
        elif 45 <= age <= 55:
            bill = 0
            print("Have Free Ride With US")
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


def true_love(male: str, female: str):
    true = "true"
    love = "love"
    male = male.lower()
    female = female.lower()
    merged_names = male + female
    total_true = 0
    total_love = 0
    for char in true:
        count = merged_names.count(char)
        total_true += count

    for char in love:
        count = merged_names.count(char)
        total_love += count
    total = total_true + total_love
    print("Total True:", total_true)
    print("Total Love:", total_love)
    print("Total", total)
    return int(f"{total_true}{total_love}")


love_score = true_love("Nagah", "Rehab")

if love_score < 10 or love_score > 90:
    print("Go together")

elif (love_score >= 40) and (love_score <= 50):
    print("Your are alright together")

else:
    print("Your Score is {}".format(love_score))
