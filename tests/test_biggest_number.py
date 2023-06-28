from src.exercises_2.biggest_number import biggest_number


def test_find_biggest_number():
    assert biggest_number(2, 3) == 3
    assert biggest_number(6, 5) == 6
    assert biggest_number(4, 4) == 4
    assert biggest_number(-1, 0) == 0
    assert biggest_number(-1, -2) == -1
