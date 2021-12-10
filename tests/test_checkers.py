from pyroy import checkers


def test_regexp_match() -> None:
    string_pattern = r'One|1'
    string_checker = checkers.RegExpMatch(string_pattern)

    assert string_checker('One') is True
    assert string_checker('1') is True
    assert string_checker('Two') is False
    assert string_checker('-1') is False

    binary_pattern = string_pattern.encode('utf-8')
    binary_checker = checkers.RegExpMatch(binary_pattern)

    assert binary_checker(b'One') is True
    assert binary_checker(b'1') is True
    assert binary_checker(b'Two') is False
    assert binary_checker(b'-1') is False
