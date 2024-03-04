import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(sec):
    print(f"Time take {sec} in seconds")
    time.sleep(sec)
    return sec


def poolDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func, 3)
        future2 = executor.submit(func, 2)
        future3 = executor.submit(func, 4)
        print(future1.result())
        print(future2.result())
        print(future3.result())


poolDemo()