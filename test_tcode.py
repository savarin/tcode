import tcode


def test_encode_string():
    assert tcode.encode_string('foo') == '+foo\n'
    assert tcode.encode_string('') == '+\n'
    assert tcode.encode_string(None) == '~\n'
    assert tcode.encode_string('foo\n') == '4foo\n\n'

def test_decode_string():
    assert tcode.decode_string('+foo\n', 0) == ['foo', 5]
    assert tcode.decode_string('+\n', 0) == ['', 2]
    assert tcode.decode_string('~\n', 0) == [None, 2]
    assert tcode.decode_string('4foo\n\n', 0) == ['foo\n', 6]
    
    assert tcode.decode_string('+foo\n+bar\n', 0) == ['foo', 5]
    assert tcode.decode_string('4foo\n\n+bar\n', 0) == ['foo\n', 6]
    
