"""
created by Nagaj at 19/06/2021
"""
fruits_dict = {"apple": 4, "banana": 1}


class Fruit:
    def __init__(self, args: dict):
        for k in args:
            setattr(self, k, args[k])  # self.apple = 4 & self.banana = 1

    def __getitem__(self, item):  # fruit['apple'] ==> item is apple
        return getattr(self, item)  # self.item =  self.apple


fruit = Fruit(fruits_dict)
print(fruit)
print(fruit["apple"])  # 4
print(fruit.apple)  # 4
