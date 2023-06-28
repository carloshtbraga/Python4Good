from src.exercises_2.is_prime import is_prime
from src.exercises_2.contains_only_even import contains_only_even
from src.exercises_2.count_digits import count_digits
from src.exercises_2.sum_digits import sum_digits
from src.exercises_2.is_pangram import is_pangram
from src.exercises_2.power import power
from src.exercises_2.find_perfect_numbers import find_perfect_numbers
from src.exercises_2.is_perfect_square import is_perfect_square
from src.exercises_2.calculate_bmi import calculate_bmi
from src.exercises_2.contains_only_uppercase import contains_only_uppercase
from src.exercises_2.calculate_age import calculate_age
from src.exercises_2.is_anagram import is_anagram
import datetime
import pytest


def test_is_prime():
    assert is_prime(7)
    assert not is_prime(15)


def test_contains_only_even():
    assert contains_only_even([2, 4, 6, 8])
    assert not contains_only_even([1, 3, 5, 7])


def test_count_digits():
    assert count_digits(12345) == 5
    assert count_digits(-9876) == 4


def test_sum_digits():
    assert sum_digits(12345) == 15
    assert sum_digits(-9876) == 30


def test_is_pangram():
    assert is_pangram("The quick brown fox jumps over the lazy dog")
    assert not is_pangram("Hello, World!")


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1


def test_find_perfect_numbers():
    assert find_perfect_numbers(1, 100) == [6, 28]
    assert find_perfect_numbers(1, 1000) == [6, 28, 496]


def test_is_perfect_square():
    assert is_perfect_square(25)
    assert not is_perfect_square(18)


def test_calculate_bmi():
    assert calculate_bmi(70, 1.75) == pytest.approx(22.86, abs=0.01)
    assert calculate_bmi(80, 1.65) == pytest.approx(29.38, abs=0.01)


def test_contains_only_uppercase():
    assert contains_only_uppercase("HELLO")
    assert not contains_only_uppercase("Hello")


def test_calculate_age():
    birthdate1 = datetime.date(1990, 5, 10)
    assert calculate_age(birthdate1) == 33

    birthdate2 = datetime.date(2005, 12, 25)
    assert calculate_age(birthdate2) == 18


def test_is_anagram():
    assert is_anagram("listen", "silent")
    assert not is_anagram("hello", "world")
