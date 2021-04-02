import json


john = {
    "name": "John",
    "age": 18,
    "degrees": [{"math": 45}, {"CS": 50}, {"English": 90}],
}

total = 0


def get_value(single_subject: dict):
    return list(single_subject.values())[0]


for subject in john["degrees"]:
    total += get_value(subject)


print(total)

print("#" * 50)
students = {
    "Harry": 81,
    "Ron": 78,
    "Herm": 99,
    "Draco": 74,
    "Neville": 62,
    "James": 300,
}
degrees = dict()


def get_degree(score: int):
    if score not in range(1, 101):
        return "Unknown"
    if score in range(51):
        return "Failed"
    if score in range(51, 66):
        return "Passed"
    if score in range(66, 76):
        return "Good"
    if score in range(76, 86):
        return "Very Good"
    if score in range(86, 101):
        return "Excellent"


info = []
for student in students:
    degree = get_degree(students[student])
    single_student = {"name": student, "score": students[student], "degree": degree}
    info.append(single_student)


def pretty_print(json_obj):
    return json.dumps(json_obj, indent=4)


print(pretty_print(info))
