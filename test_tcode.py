import tcode


def test_encode_unit():
    assert tcode.encode_unit('foo') == '+foo\n'
    assert tcode.encode_unit('') == '~\n'
    assert tcode.encode_unit('foo\n') == '4foo\n\n'

def test_decode_unit():
    assert tcode.decode_unit('+foo\n') == ['foo', 4]
    assert tcode.decode_unit('~\n') == ['', 1]
    assert tcode.decode_unit('4foo\n\n') == ['foo\n', 5]
