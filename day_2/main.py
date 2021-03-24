from anat import Category


class MainApp:
    @staticmethod
    def run():
        clothes = Category("Clothes")
        medicines = Category("Medicines")
        print(clothes)
        print(medicines)
        Category.insert_obj(clothes)
        obj = Category.find_by_id(_id=clothes.uuid)
        # obj.export_to_text()
        obj.export_to_json()
        Category.delete_obj(_id=clothes.uuid)
        print(obj == clothes)


if __name__ == "__main__":
    MainApp.run()
