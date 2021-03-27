colors = {
    "red": [{"rgb": (241, 49, 7), "hex": "#F13107"}],
    "black": [{"rgb": (14, 14, 14), "hex": "#0E0E0E"}],
    "green": [{"rgb": (5, 109, 33), "hex": "#056D21"}],
}


def get_color(color: str):
    if colors.get(color) is not None:
        return colors[color]
    else:
        raise KeyError(f"Should be one of <{list(colors.keys())}>")


print(get_color("green"))
print(get_color("blue"))  # key error
