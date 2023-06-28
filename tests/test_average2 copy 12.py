from src.average import find_average


def test_average():
    assert find_average([1, 1, 1]) == 1
    assert find_average([7.5, 8, 8.5]) == 8
    assert find_average([0, 10, 0]) == 10/3
    assert find_average([10, 10, 10]) == 10
    assert find_average([40, 50, 30]) == (40 + 50 + 30) / 3
