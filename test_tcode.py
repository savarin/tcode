import tcode


def test_encode_unit():
    assert tcode.encode_unit('foo') == '+foo\n'
    assert tcode.encode_unit('') == '+\n'
    assert tcode.encode_unit(None) == '~\n'
    assert tcode.encode_unit('foo\n') == '4foo\n\n'

def test_decode_unit():
    assert tcode.decode_unit('+foo\n', 0) == ['foo', 5]
    assert tcode.decode_unit('+\n', 0) == ['', 2]
    assert tcode.decode_unit('~\n', 0) == [None, 2]
    assert tcode.decode_unit('4foo\n\n', 0) == ['foo\n', 6]
    
    assert tcode.decode_unit('+foo\n+bar\n', 0) == ['foo', 5]
    assert tcode.decode_unit('4foo\n\n+bar\n', 0) == ['foo\n', 6]
    
