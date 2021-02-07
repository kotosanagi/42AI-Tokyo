def count_character(s):
    num = 0
    for c in s:
        num += 1
    return num


def count_upper(s):
    num = 0
    for c in s:
        if c.isupper():
            num += 1
    return num


def count_lower(s):
    num = 0
    for c in s:
        if c.islower():
            num += 1
    return num


def count_punctuation(s):
    num = 0
    for c in s:
        if c == '.' or c == ',':
            num += 1
    return num


def count_space(s):
    num = 0
    for c in s:
        if c == ' ':
            num += 1
    return num


def text_analyzer(*args):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
    n_len = len(args)
    print(args)
    print(n_len)
    if n_len > 1:
        print("ERROR")
        return
    if n_len == 1:
        s = args[0]
    elif n_len == 0:
        s = input("What is the text to analyse?\n")
    print("The text contains " + str(count_character(s)) + " characters:")
    print("- " + str(count_upper(s)) + " upper letters")
    print("- " + str(count_lower(s)) + " lower letters")
    print("- " + str(count_punctuation(s)) + " punctuation marks")
    print("- " + str(count_space(s)) + " spaces")
