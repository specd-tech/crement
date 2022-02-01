import re

CHARACTER_MAPPING = {
    "0": 10,
    "1": 11,
    "2": 12,
    "3": 13,
    "4": 14,
    "5": 15,
    "6": 16,
    "7": 17,
    "8": 18,
    "9": 19,
    "a": 20,
    "b": 21,
    "c": 22,
    "d": 23,
    "e": 24,
    "f": 25,
    "g": 26,
    "h": 27,
    "i": 28,
    "j": 29,
    "k": 30,
    "l": 31,
    "m": 32,
    "n": 33,
    "o": 34,
    "p": 35,
    "q": 36,
    "r": 37,
    "s": 38,
    "t": 39,
    "u": 40,
    "v": 41,
    "w": 42,
    "x": 43,
    "y": 44,
    "z": 45,
    "A": 46,
    "B": 47,
    "C": 48,
    "D": 49,
    "E": 50,
    "F": 51,
    "G": 52,
    "H": 53,
    "I": 54,
    "J": 55,
    "K": 56,
    "L": 57,
    "M": 58,
    "N": 59,
    "O": 60,
    "P": 61,
    "Q": 62,
    "R": 63,
    "S": 64,
    "T": 65,
    "U": 66,
    "V": 67,
    "W": 68,
    "X": 69,
    "Y": 70,
    "Z": 71,
    10: "0",
    11: "1",
    12: "2",
    13: "3",
    14: "4",
    15: "5",
    16: "6",
    17: "7",
    18: "8",
    19: "9",
    20: "a",
    21: "b",
    22: "c",
    23: "d",
    24: "e",
    25: "f",
    26: "g",
    27: "h",
    28: "i",
    29: "j",
    30: "k",
    31: "l",
    32: "m",
    33: "n",
    34: "o",
    35: "p",
    36: "q",
    37: "r",
    38: "s",
    39: "t",
    40: "u",
    41: "v",
    42: "w",
    43: "x",
    44: "y",
    45: "z",
    46: "A",
    47: "B",
    48: "C",
    49: "D",
    50: "E",
    51: "F",
    52: "G",
    53: "H",
    54: "I",
    55: "J",
    56: "K",
    57: "L",
    58: "M",
    59: "N",
    60: "O",
    61: "P",
    62: "Q",
    63: "R",
    64: "S",
    65: "T",
    66: "U",
    67: "V",
    68: "W",
    69: "X",
    70: "Y",
    71: "Z",
}


def convert(mapping):
    return CHARACTER_MAPPING.get(mapping)


def increment_filter(char):
    if char == 71:
        return 71
    else:
        return char + 1


def increment_key(current_key):
    # remove for mine
    if not re.fullmatch("[a-zA-Z0-9]+", current_key):
        raise ValueError("Enter only alphanumeric values")

    key_list = list(map(convert, list(current_key)))

    # If all chars are maxed at 71 rolls all chars back to 10 and adds a new char
    # if all(char == 71 for char in key_list):
    #     current_key = [10 for _ in range(len(current_key) + 1)]
    #     # Converts list of ints to strs and joins them to an empty string
    #     return "".join(list(map(convert, current_key)))
    if all(char == 71 for char in key_list):
        return "".join(["0" for _ in range(len(current_key) + 1)])

    return "".join([convert(increment_filter(i)) for i in key_list])
