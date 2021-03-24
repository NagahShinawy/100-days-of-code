import uuid
from utils.errors import NotFoundObj


class CRUD:
    @classmethod
    def find_by_id(cls, _id):
        for obj in cls.objs:
            if obj.uuid == _id:
                return obj
        raise NotFoundObj(f"category of id <{_id}> not found")

    @classmethod
    def delete_obj(cls, _id):
        obj = cls.find_by_id(_id)
        cls.objs.remove(obj)


class Category(CRUD):
    objs = []

    def __init__(self, category_name):
        self.category_name = category_name
        self.uuid = uuid.uuid4()
        Category.objs.append(self)

    def __repr__(self):
        return f"<{self.uuid}><{self.category_name}>"


if __name__ == "__main__":
    clothes = Category("Clothes")
    medicines = Category("Medicines")
    print(clothes)
    print(medicines)
    obj = Category.delete_obj(_id=clothes.uuid)
    obj = Category.find_by_id(_id=clothes.uuid)
    print(obj == clothes)
