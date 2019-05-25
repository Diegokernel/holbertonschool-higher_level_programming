#!/usr/bin/python3
"""
    Module with one method: text_indentation(text)
"""

def text_indentation(text):
    """
        Print text with two newlines between each punctuation and colon
        If text is not str, raise error
    """
    chars = ['.', '?', ':']
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        c = 0
        while text[c] == " ":
            c += 1
        while c < len(text):
            print(text[c], end="")
            if text[c] in chars:
                while text[c + 1] == " ":
                    c += 1
                print()
                print()
            c += 1
