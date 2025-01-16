from src.app import process_list


def test_process_list_given_list_of_positive_ints():
    result = process_list([9, 1, 2, 3, 4, 4, 6, 7])
    assert result == [1, 4, 9, 16, 16, 36, 49, 81]


def test_process_list_given_list_with_negative_ints():
    result = process_list([-9, 1, 2, 3, -4, 4, 6, 7])
    assert result == [81, 16, 1, 4, 9, 16, 36, 49]


def test_process_list_given_empty_list():
    result = process_list([])
    assert result == []
