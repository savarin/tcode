import tcode


def test_encode_unit():
    assert tcode.encode_unit('foo') == '+foo\n'
    assert tcode.encode_unit('') == '~\n'
    assert tcode.encode_unit('foo\n') == '4foo\n\n'
