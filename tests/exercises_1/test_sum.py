from src.exercises_1.sum import sum


def test_sum():
    assert sum(5, 5) == 10
    assert sum(0, 0) == 0
    assert sum(-1, -1) == -2
