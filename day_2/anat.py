import json
import uuid
from utils.errors import ObjNotFound, InsertError


class CRUD:
    @classmethod
    def find_by_id(cls, _id):
        for obj in cls.objs:
            if obj.uuid == _id:
                return obj
        raise ObjNotFound(f"category of id <{_id}> not found")

    @classmethod
    def delete_obj(cls, _id):
        obj = cls.find_by_id(_id)
        cls.objs.remove(obj)

    @classmethod
    def insert_obj(cls, obj):
        if not isinstance(obj, cls):
            raise InsertError(
                f"can not insert obj of type <{obj.__class__.__name__}> only, <{cls}>"
            )
        cls.objs.append(obj)


class Export:
    def export_to_text(self):
        with open(f"{self}.txt", "w") as f:
            f.write(self.__to_string())

    def __to_string(self):
        return str(self)

    def export_to_word(self):
        pass

    def export_to_json(self):
        obj = self.__dict__
        if obj.get("uuid") is not None:
            obj.update({"uuid": str(obj["uuid"])})
            with open(f"{self}.json", "w") as f:
                f.write(json.dumps(obj, indent=4))
        else:
            raise TypeError("JSON is not serializable")


class Category(CRUD, Export):
    objs = []

    def __init__(self, category_name):
        self.category_name = category_name
        self.uuid = uuid.uuid4()

    def __repr__(self):
        return f"[{self.uuid}][{self.category_name}]"
