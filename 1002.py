from collections import Counter
from typing import List

words = ["bella","label","roller"]

common = Counter(words[0])
print(common)
print( list(common.elements()) )