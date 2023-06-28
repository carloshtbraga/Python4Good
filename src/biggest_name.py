from typing import List


def find_biggest_name(names: List[str]) -> str:
    biggestName = ''
    for name in names:
        if len(name) > len(biggestName):
            biggestName = name
    return biggestName


print(find_biggest_name(['Leco, bico, Josué, Carlinhos']))
