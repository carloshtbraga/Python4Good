from src.exercises_2.average import average


def test_average():
    assert average([5, 5, 5]) == 5
    assert average([7.5, 8, 8.5]) == 8
    assert average([0, 10, 0]) == 10/3
    assert average([-1, -1, -1]) == -1
