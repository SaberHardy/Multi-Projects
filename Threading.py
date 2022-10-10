import threading
import time

"""
To create a thread we should make a function that act like a thread.
"""

list_items = []


def first_threading_func(n):
    for i in range(1, n + 1):
        list_items.append(i)
        time.sleep(0.5)


def second_threading_func(n):
    for i in range(1, n + 1):
        list_items.append(i)
        time.sleep(0.9)


x = threading.Thread(target=first_threading_func, args=(5,))
x.start()

y = threading.Thread(target=first_threading_func, args=(5,))
y.start()

print(f"Number of processors used: {threading.activeCount()}")
print(list_items)
# the result is [1,1] why? => this is because the two of threads is slept
