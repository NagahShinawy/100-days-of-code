from anat import Category, User


class MainApp:
    @staticmethod
    def run():
        clothes = Category("Clothes")
        food = Category("Food")

        Category.insert(clothes)
        Category.insert(food)
        # Category.insert(food)

        obj = Category.find_by_id(_id=clothes.uuid)
        obj.to_json()
        Category.update(_id=clothes.uuid, updated_obj=food)
        Category.delete(_id=food.uuid)

        # ########################################
        user = User(username="Nagah", dob="2000-03-09")
        user.to_json()
        # user2 = User(username="Ahmed", dob="2000-03-09")
        # User.insert(user)
        # User.update(user.uuid, user2)
        # print(User.objs)
        # User.delete(_id=user2.uuid)
        # print(User.objs)


if __name__ == "__main__":
    MainApp.run()
