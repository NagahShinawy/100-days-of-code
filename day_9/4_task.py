travel_logs = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Paris", "Lille", "Dijon"]},
]


def add_new_country(country: str, visits: int, *cities):
    travel_log = {"country": country, "visits": visits, "cities": cities}
    travel_logs.append(travel_log)


print(travel_logs)

print("#" * 50)

add_new_country("Egypt", 8, "Cairo", "Giza")

print(travel_logs)


def to_json(travels):
    import json

    with open("travels.json", "w") as file:
        file.write(json.dumps(travels, indent=4))


to_json(travel_logs)
