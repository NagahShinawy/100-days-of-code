from random import seed, randint


def seed_number() -> None:
    testseed = int(input("Create Seed"))

    seed(testseed)


def get_names() -> list:
    names = input("Type Names Separated by comma")
    return [name.strip() for name in names.split(",")]


def get_random_name(names: list) -> str:
    random_index = randint(0, len(names) - 1)
    return names[random_index]


def main():
    seed_number()
    names = get_names()
    person_who_will_pay = get_random_name(names)
    print(person_who_will_pay, "Is Going To Buy a Meal Today")


if __name__ == "__main__":
    main()
