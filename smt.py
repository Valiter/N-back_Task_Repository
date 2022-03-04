import time


def time_func():
    a = 0
    start = time.monotonic()
    while a < 10:
        result = time.monotonic() - start
        if 2 < result:
            print(start)
            print(result)
            print("Program time: {:>.3f}".format(result) + " seconds.")
            a += 1
            start = time.monotonic()


time_func()
