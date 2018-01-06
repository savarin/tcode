def encode_unit(string):
    result = ''
    simple = True

    for i, char in enumerate(string):
        if char == '\n':
            simple = False
        result += char
    result += '\n'

    if not string:
        return '~' + result
    elif simple:
        return '+' + result
    return str(i + 1) + result
