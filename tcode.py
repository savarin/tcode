from datetime import datetime


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


def decode_unit(string, offset=0):
    string = string[offset:]
    result = ''

    if string[0] == '~':
        assert len(string) == 2
        return [None, 2]

    elif string[0] == '+':
        for i, char in enumerate(string[1:]):
            if char == '\n':
                return [result, i+2+offset]
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

    return [result, i+int(length)+1+offset]


def decode_stream(string, offset=0, count=None):
    result = []
    counter = 0

    while offset < len(string):
        unit, offset = decode_unit(string, offset)
        result.append(unit)
    
    return result


def encode_list(types, units):
    result = ''
    assert len(types) == len(units)

    for i, unit in enumerate(units):
        if types[i] == 'str':
            result += encode_unit(unit)
        elif types[i] == 'int':
            result += encode_unit(str(unit))
        elif types[i] == 'date':
            result += encode_unit(unit.strftime('%Y%m%d'))

    return result


def decode_list(types, string, offset=0):
    result = []
    stream = decode_stream(string, offset)

    for i, unit in enumerate(stream):
        if types[i] == 'str':
            result.append(unit)
        elif types[i] == 'int':
            result.append(int(unit))
        elif types[i] == 'date':
            result.append(datetime.strptime(unit, '%Y%m%d').strftime('%Y-%m-%d'))

    return result
