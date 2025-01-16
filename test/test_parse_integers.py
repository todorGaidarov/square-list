from src.app import parse_integers_from_string


def test_parse_integers_from_string_given_valid_positive_ints_input():
    result = parse_integers_from_string("12 3 5 112 456 2")
    expected_output = [12, 3, +5, 112, +456, 2]
    assert result == expected_output


def test_parse_integers_from_string_given_negative_ints_input():
    result = parse_integers_from_string("-12 +3 5 -112 -456 2")
    expected_output = [-12, 3, 5, -112, -456, 2]
    assert result == expected_output


def test_parse_integers_from_string_given_invalid_input():
    result = parse_integers_from_string("112ds")
    assert result is None

    result = parse_integers_from_string("- 222")
    assert result is None

    result = parse_integers_from_string("       ")
    assert result is None


def test_parse_integers_from_string_given_empty_string():
    result = parse_integers_from_string("")
    assert result is None


def test_parse_integers_from_string_given_single_int():
    result = parse_integers_from_string("1")
    assert result == [1]


def test_parse_integers_from_string_given_zeros():
    result = parse_integers_from_string("   0     0 0 0 ")
    assert result == [0, 0, 0, 0]
