"""
created by Nagaj at 16/05/2021
"""


class User:
    def __init__(self, userid, username):
        self.username = username
        self.userid = userid
        self.followers = []
        self.following = []
        print(f"new user {self} created ..")

    def follow(self, user):
        if self != user and user not in self.following:
            self.following.append(user)
            user.followers.append(self)

    def unfollow(self, user):
        if self != user and user in self.following:
            self.following.remove(user)
            user.followers.remove(self)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username


user_1 = User("001", "john")
user_2 = User("002", "james")
user_3 = User("003", "leon")
user_4 = User("004", "jack")

print(user_1.followers)
print(user_2.followers)
print(user_3.followers)

user_1.follow(user_2)
user_1.follow(user_2)
user_1.follow(user_3)
user_1.follow(user_1)
user_1.follow(user_4)

print(user_1.following)

print(user_2.followers)
print(user_3.followers)
print(user_4.followers)

user_1.unfollow(user_2)

print(user_1.following)
print(user_2.followers)
print(user_3.followers)

user_1.unfollow(user_3)
print(user_3.followers)
# user_1.id = "001"
# user_1.username = "john"
# user_1.email = "john@test.com"
# print(user_1)
#
# print("ID", user_1.id)
# print("username", user_1.username)
# print("Email", user_1.email)
#
# print("#" * 100)
# user_2.id = "002"
# user_2.username = "james"
# user_2.email = "james@test.com"
# print(user_2.username)
#
# print("#" * 100)
#
# user_3.id = "003"
# user_3.username = "leon"
# user_3.email = "lean@test.com"
# print(user_3.username)
