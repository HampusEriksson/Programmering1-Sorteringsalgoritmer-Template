"""
Implementera bubble sort
https://www.youtube.com/watch?v=xli_FI7CuzA&list=PL9xmBV_5YoZOZSbGAXAPIq1BeUf4j20pl&index=4&ab_channel=MichaelSambol
Bubble sort är en enkel sorteringsalgoritm där varje element jämförs med det nästkommande elementet och byter plats om de är i fel ordning. 
Den största (eller minsta) kommer att "bubbla" upp (eller ner) till rätt position för varje iteration.
"""

import random


def bubble_sort(list_to_sort):
    pass


numbers = [random.randint(0, 1000) for _ in range(100)]

print(numbers)
bubble_sort(numbers)
print(numbers)
