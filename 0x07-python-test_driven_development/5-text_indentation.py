#!/usr/bin/python3
""" this module contains one function called ``text_indentation()`` """


def text_indentation(text):

    """ the function prints two newlines after if it catches
        . or : or ? in the text given to the function
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    res = []
    sentence = ""
    for char in text:
        sentence += char
        if char in '.?:':
            res.append(sentence.strip() + '\n\n')
            sentence = ""
    res.append(sentence.strip())

    return ''.join(res)
