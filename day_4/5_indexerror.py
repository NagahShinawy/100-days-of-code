#        0       1           2           3           4     5
apps = ["FB", "Instgram", "Youtube", "Twitter", "WhatsApp"]


print(len(apps))
last_index = len(apps) - 1
print(apps[last_index])
last_index = -1

print(apps[last_index])


# Nested list
social_media_apps = ["FB", "Instgram", "Twitter"]
chatting_apps = ["WhatsApp", "Telegram", "Messenger"]

apps = [social_media_apps, chatting_apps]

print(apps[0][0])
print(apps[0][1])
print(apps[1][1])
