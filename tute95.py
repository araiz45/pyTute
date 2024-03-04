import time
from concurrent.futures import ThreadPoolExecutor

def func(sec):
    print(f"Time take {sec} in seconds")
    time.sleep(sec)
    return sec


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        l = [4, 6, 3, 6, 3, 6, 3]
        results = executor.map(func, l)
        for result in results:
            print(result)

poolingDemo()