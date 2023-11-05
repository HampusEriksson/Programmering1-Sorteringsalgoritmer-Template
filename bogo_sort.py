"""
Implementera bogo sort
BogoSort  omplacerar slumpmässigt elementen i listan.
Efter varje omplacering kontrollerar algoritmen om listan är ordnad. 
Om den inte är det, blandar den om listan igen och fortsätter processen tills listan är sorterad.
"""

import random


def bogo_sort(list_to_sort):
    pass


numbers = [random.randint(0, 1000) for _ in range(100)]

print(numbers)
bogo_sort(numbers)
print(numbers)
