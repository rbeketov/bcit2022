from contextlib import contextmanager
import time

from unicodedata import name

@contextmanager
def cm_timer_1():
    start_time = time.time()
    yield
    print("time: ", time.time() - start_time)

class cm_timer_2:
    def __init__(self):
        self.start_time = 0
    def __enter__(self):
        self.start_time = time.time()
    def __exit__(self, type, value, traceback):
        print("time: ", time.time() - self.start_time)

if __name__ == "__main__":

    with cm_timer_1():
        time.sleep(1.5)

    with cm_timer_2():
        time.sleep(1.5)