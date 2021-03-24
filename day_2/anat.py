import json
import uuid
from utils.errors import ObjNotFound, InsertError, ObjAlreadyExists


class Export:
    def to_txt(self):
        with open(f"{self}.txt", "w") as f:
            f.write(self.__to_string())

    def __to_string(self):
        return json.dumps(
            self, default=lambda obj: obj.__dict__, sort_keys=True, indent=4
        )

    def to_word(self):
        pass

    def to_json(self):
        with open(f"{self}.json", "w") as f:
            f.write(self.__to_string())


class CRUD:
    objs = []

    @classmethod
    def find_by_id(cls, _id):
        for obj in cls.objs:
            if obj.uuid == _id:
                return obj
        raise ObjNotFound(f"category of id <{_id}> not found")

    @classmethod
    def delete(cls, _id):
        obj = cls.find_by_id(_id)
        cls.objs.remove(obj)

    @classmethod
    def insert(cls, obj):
        if not isinstance(obj, cls):
            raise InsertError(
                f"can not insert obj of type <{obj.__class__.__name__}> only, <{cls}>"
            )
        if obj in cls.objs:
            raise ObjAlreadyExists(f"{obj} exists")

        cls.objs.append(obj)

    @classmethod
    def update(cls, _id, updated_obj):
        obj = cls.find_by_id(_id)
        cls.objs[cls.objs.index(obj)] = updated_obj  # replace


class Category(CRUD, Export):
    objs = []

    def __init__(self, category_name):
        self.category_name = category_name
        self.uuid = uuid.uuid4()

    def __repr__(self):
        return f"[{self.uuid}][{self.category_name}]"


class User(CRUD):
    def __init__(self, username, dob):
        self.uuid = uuid.uuid4()
        self.username = username
        self.dob = dob

    def __repr__(self):
        return f"[{self.username}][{self.dob}]"
