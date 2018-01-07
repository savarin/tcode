def encode_string(string):
    if string is None:
        return '~\n'

    result = ''
    simple = True

    for i, char in enumerate(string):
        if char == '\n':
            simple = False
        result += char
    result += '\n'

    if simple:
        return '+' + result
    return str(i + 1) + result


def decode_string(string, offset):
    string = string[offset:]
    result = ''

    if string[0] == '~':
        assert len(string) == 2
        return [None, 2]

    elif string[0] == '+':
        for i, char in enumerate(string[1:]):
            if char == '\n':
                return [result, i+2]
            result += char

    digits = set([str(i) for i in xrange(10)])
    length = ''

    for i, char in enumerate(string):
        if char in digits:
            length += char
        else:
            break
            
    result = string[i:i+int(length)]
    assert string[i+int(length)] == '\n'

    return [result, i+int(length)+1]
