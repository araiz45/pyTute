from functools import lru_cache

import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n + 4


print(fx(4))
print("Done for 4")
print(fx(5))
print("done for 5")
print(fx(6))
print("Done for 6")


print(fx(4))
print("Done for 4")
print(fx(5))
print("done for 5")
print(fx(6))
print("Done for 6")