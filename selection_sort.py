"""
Implementera selection sort
https://www.youtube.com/watch?v=g-PGLbMth_g&list=PL9xmBV_5YoZOZSbGAXAPIq1BeUf4j20pl&index=2&ab_channel=MichaelSambol
Selection sort fungerar genom att successivt hitta det minsta elementet från det osorterade avsnittet och placera det i början av listan.
Det fungerar genom att upprepa processen att hitta det näst minsta elementet i resten av listan. 
"""

import random


def selection_sort(list_to_sort):
    pass


numbers = [random.randint(0, 1000) for _ in range(100)]

print(numbers)
selection_sort(numbers)
print(numbers)
