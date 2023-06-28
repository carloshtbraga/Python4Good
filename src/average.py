from typing import List


def find_average(numbers: List[int]) -> float:
    counter = 0
    for number in numbers:
        counter += number
    return counter / len(numbers)


print(find_average([10, 10, 10]))
