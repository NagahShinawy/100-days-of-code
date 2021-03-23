import re


class NationalId:
    def __init__(self, national_id):
        self.national_id = national_id

    @property
    def national_id(self):
        return self.usernational_id

    @national_id.setter
    def national_id(self, _id):
        is_valid = re.findall(r"^\d{14}$", _id)
        if is_valid:
            self.usernational_id = is_valid[0]
        else:
            raise ValueError(f"Invalid National ID {_id}")


if __name__ == "__main__":
    user = NationalId("12345678908762")
    print(user.national_id)
