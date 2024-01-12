#!/usr/bin/python3
roman_keys = {
    'I': 0,
    'V': 1,
    'X': 2,
    'L': 3,
    'C': 4,
    'D': 5,
    'M': 6,
}

roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_int(roman_string: str) -> int:
    """converts roman numeral to string
    :param roman_string - roman numeral
    :return roman numeral as integer
    """
    value = 0
    if not isinstance(roman_string, str):
        return 0
    for idx, char in enumerate(roman_string):
        # check if it's a valid char
        if roman_keys.get(char.upper(), -1) == -1:
            return 0
        # check whether you're at the end of the string
        if idx != (len(roman_string) - 1):
            # determines whether to do positive or negative addition
            current_char_weight = roman_keys.get(char.upper(), -1)
            next_char_weight = roman_keys[roman_string[idx + 1].upper()]
            intRepOfChar = roman_values[char.upper()]
            if current_char_weight >= next_char_weight:
                value += intRepOfChar
            else:
                value -= intRepOfChar
        else:
            value += roman_values[char.upper()]
    return value
