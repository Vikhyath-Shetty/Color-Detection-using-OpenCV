from type import ColorInput

# Functions to check if the color(param) is valid
# Checks for both str | ColorInput -> set of {"red","green","blue","yellow"}


def is_color(color: ColorInput) -> bool:
    return color in {"red", "green", "blue", "yellow"}


def is_color_set(color: ColorInput) -> bool:
    if isinstance(color, set):
        return True
    else:
        return False


def is_color_input(color: ColorInput) -> bool:
    return is_color(color) or is_color_set(color)
