def encode_unit(string):
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


def decode_unit(string):
    if string[0] == '~':
        assert len(string) == 2
        return [None, 1]

    digits = set([str(i) for i in xrange(10)])
    result = ''
    length = ''
    bulk = False

    for i, char in enumerate(string):
        if not i and char in digits:
            bulk = True
            length += char
            continue
        elif bulk and char in digits:
            length += char
            continue
        elif bulk and char not in digits:
            bulk = False

        result += char

    assert result[-1] == '\n'

    if result[0] == '+':
        result = result[1:-1]
    else:
        assert length
        assert len(result) == int(length) + 1
        result = result[:-1]

    return [result, i]
