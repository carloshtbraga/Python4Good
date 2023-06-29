from src.exercises_1.fahrenheit import fahrenheit
from src.exercises_1.sum import sum
from src.exercises_1.is_even import is_even
from src.exercises_1.check_number_sign import check_number_sign
from src.exercises_1.is_palindrome import is_palindrome
from src.exercises_1.factorial import factorial
from src.exercises_1.count_vowels import count_vowels
from src.exercises_1.is_sorted import is_sorted
from src.exercises_1.has_common_elements import has_common_elements
from src.exercises_1.average import average
from src.exercises_1.biggest_number import biggest_number
from src.exercises_1.biggest_name import biggest_name


def test_fahrenheit():
    assert fahrenheit(50) == 122
    assert fahrenheit(33) == 91.4


def test_sum():
    assert sum(5, 5) == 10
    assert sum(0, 0) == 0
    assert sum(-1, -1) == -2


def test_is_even():
    assert is_even(4)
    assert not is_even(7)


def test_check_number_sign():
    assert check_number_sign(5) == "Positivo"
    assert check_number_sign(-2) == "Negativo"
    assert check_number_sign(0) == "Zero"


def test_is_palindrome():
    assert is_palindrome("radar")
    assert not is_palindrome("python")


def test_factorial():
    assert factorial(5) == 120


def test_count_vowels():
    assert count_vowels("Hello, World!") == 3


def test_is_sorted():
    assert is_sorted([1, 2, 3, 4])
    assert not is_sorted([4, 2, 5, 1, 6])


def test_has_common_elements():
    assert not has_common_elements([1, 2, 3], [4, 5, 6])
    assert has_common_elements([1, 2, 3], [3, 4, 5, 6])


def test_average():
    assert average([5, 5, 5]) == 5
    assert average([7.5, 8, 8.5]) == 8
    assert average([0, 10, 0]) == 10 / 3
    assert average([-1, -1, -1]) == -1


def test_find_biggest_name():
    first_name_list = ["José", "Lucas", "Nádia", "Fernanda"]
    second_name_list = ["José", "Nádia", "João"]
    third_name_list = ["Henrique", "João"]
    fourth_name_list = ["José", "João"]
    assert biggest_name(first_name_list) == "Fernanda"
    assert biggest_name(second_name_list) == "Nádia"
    assert biggest_name(third_name_list) == "Henrique"
    #  First odccurrence prevails
    assert biggest_name(fourth_name_list) == "José"


def test_find_biggest_number():
    assert biggest_number(2, 3) == 3
    assert biggest_number(6, 5) == 6
    assert biggest_number(4, 4) == 4
    assert biggest_number(-1, 0) == 0
    assert biggest_number(-1, -2) == -1
