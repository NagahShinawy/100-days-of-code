"""
created by Nagaj at 21/05/2021
"""


class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("inhale, exhale")

    def __str__(self):
        return f"<obj><{self.__class__.__name__}>"


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing This Under Water")

    def swim(self):
        print("moving in water")


cat = Animal()
nemo = Fish()

nemo.breathe()
print("#" * 30)
nemo.swim()
print("#" * 30)
print("Eyes:", nemo.eyes)
print("#" * 30)
print(nemo)
print(cat)
