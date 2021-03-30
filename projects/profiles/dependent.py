class Child:

    GENDER = ["MALE", "FEMALE"]

    def __init__(self, name, gender):
        self.childname = name
        self.gender = gender

    def __repr__(self):
        return self.childname

    def to_json(self):
        return {"name": self.childname, "gender": self.gender}

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):

        if gender not in self.GENDER:
            raise ValueError("Just MALE or FEMALE")
        self._gender = gender


class Parent:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child: Child):
        self.children.append(child)

    @property
    def children_profiles(self):
        return [child.to_json() for child in self.children]

    def has_a_child(self, child):
        return True if child in self.children else False

    def __repr__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not type(name) == str:
            raise ValueError("should be string not {}".format(name.__class__.__name__))

        if not name:
            raise ValueError("can not be empty string")

        self._name = name
