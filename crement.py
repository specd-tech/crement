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


def _convert(mapping: str | int) -> int | str:
    return CHARACTER_MAPPING.get(mapping)


# test with step of -1 and greater then 1 or -1
def crement(characters: str) -> str:
    if not re.fullmatch("[a-zA-Z0-9]+", characters):
        raise ValueError("Enter only alphanumeric values")

    # Converts alphanumeric characters to an int between 0-71 based on CHARACTER_MAPPING
    char_list = list(map(_convert, list(characters)))

    # Reverse char_list so the first value is the least significant character
    char_list.reverse()
    for i, char in enumerate(char_list):
        if char >= 71:
            # Resets current position to the starting value of 10
            char_list[i] = 10

            # If all places are 71, add another place and resets current char to 10
            if i == len(char_list) - 1:
                char_list.append(10)
                break

            # If the next character is not 71 then the next character will not need to be carried over so the loop
            # is broken.
            elif char_list[i + 1] != 71:
                char_list[i + 1] += 1
                break

            # Else the next character will be over 71 and need to be carried over, not breaking runs the loop again
            # to process the next character.
            else:
                char_list[i + 1] += 1

        else:
            # Increments to the last place
            char_list[i] += 1
            break

    char_list.reverse()
    # Returns reconstructed string from char_list
    return "".join(list(map(_convert, char_list)))
