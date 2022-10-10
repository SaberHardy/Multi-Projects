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


# def task(sleep_time, message):
#     time.sleep(sleep_time)
#     print(str(message))
#
#
# thread = threading.Thread(target=task, args=(3, "this is from arguments"))
# thread.start()
# print("waiting the thread!!")
# print("waiting the thread!!")
# print("waiting the thread!!")
# thread.join()

class CustomThread(threading.Thread):

    def run(self):
        time.sleep(1)
        print("This was stopped for 3 sec")
        self.value = 99
        time.sleep(1)


thread_class = CustomThread()
thread_class.name = "FirstThreadName"
thread_class.start()
print("\n\nWaiting for the thread to excute....")
print(f"is_alive is {thread_class.is_alive()}")  # True

thread_class.join()
print(f"the value from run function is {thread_class.value}")
print(f"the name is {thread_class.name}")
print(f"the daemon is {thread_class.daemon}")
print(f"the ident is {thread_class.ident}")
print(f"the native id is {thread_class.native_id}")
print(f"is_alive is {thread_class.is_alive()}")  # False
print(f"Thread name is {thread_class.name}")  # False
