def roman_to_int(roman_string):
    roman_equivalent = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    s_list = list(roman_string)
    int_value = 0

    for i in range(len(s_list)):
        if i < len(s_list) - 1 and
        roman_equivalent[s_list[i]] < roman_equivalent[s_list[i + 1]]:
            int_value -= roman_equivalent[s_list[i]]
        else:
            int_value += roman_equivalent[s_list[i]]

    return int_value
