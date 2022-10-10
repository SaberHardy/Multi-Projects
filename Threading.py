import threading
import time

"""
To create a thread we should make a function that act like a thread.
"""
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

x.join()

y = threading.Thread(target=first_threading_func, args=(5,))
y.start()

y.join()
# the result is [1,1] why? => this is because the two of threads is slept
# The solution of this problem is to use .join(this mean don't move to next
# step until finish the step before)
print(f"Number of processors used: {threading.activeCount()}")
print(list_items)
"""


def task(sleep_time, message):
    time.sleep(sleep_time)
    print(str(message))


thread = threading.Thread(target=task, args=(3, "this is from arguments"))
thread.start()
print("waiting the thread!!")
print("waiting the thread!!")
print("waiting the thread!!")
thread.join()
