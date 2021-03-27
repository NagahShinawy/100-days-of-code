fruits = ["Apple", "Orange", "Banana"]
players = ["Messi", "Ronaldo", "Mo Salah"]
apps = ["FB", "Instgram", "Youtube", "Twitter", "WhatsApp"]

counter = 1
for player in players:
    print(counter, player)
    counter += 1

print("#" * 20)

for counter, app in enumerate(apps, start=1):
    print(counter, app)

print("#" * 30)
level = "Level"
print(level + "s")
for i in range(1, 11):
    print(f"{level}#{i}")

emails = ["john@huawei.com", "sara@huawei.com", "eric@huawei.com"]

for email in emails:
    print("sending email to <{}> ....".format(email))
