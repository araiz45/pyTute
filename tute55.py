# Reduce 
from functools import reduce

number = [2, 5, 2, 5, 2, 6, 3, 4, 7, 2, 9]
sum2 = reduce(lambda x, y: x + y, number)
print(sum2)