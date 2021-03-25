class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.bmi_value = round(self.weight / self.height ** 2, 2)


class Message:
    MSG = ""
    MIN = 0
    MAX = 0


class UnderWeight(Message):
    MSG = "UnderWeight"
    MIN = 0
    MAX = 18.5


class NormalWeight(Message):
    MSG = "NormalWeight"
    MIN = 18.5
    MAX = 25


class OverWeight(Message):
    MSG = "OverWeight"
    MIN = 25
    MAX = 30


class Obese(Message):
    MSG = "Obese"

    MIN = 30
    MAX = 35


class ClinicObese(Message):
    MSG = "ClinicObese"

    MIN = 35
    MAX = 100


if __name__ == "__main__":
    pass
