import threading
from random import random
from threading import get_native_id
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

# class CustomThread(threading.Thread):
#
#     def run(self):
#         time.sleep(1)
#         print("This was stopped for 3 sec")
#         self.value = 99
#         time.sleep(1)
#
#
# thread_class = CustomThread()
# thread_class.name = "FirstThreadName"
# thread_class.start()
# print("\n\nWaiting for the thread to excute....")
# print(f"is_alive is {thread_class.is_alive()}")  # True
#
# thread_class.join()
# print(f"the value from run function is {thread_class.value}")
# print(f"the name is {thread_class.name}")
# print(f"the daemon is {thread_class.daemon}")
# print(f"the ident is {thread_class.ident}")
# print(f"the native id is {thread_class.native_id}")
# print(f"is_alive is {thread_class.is_alive()}")  # False
# print(f"Thread name is {thread_class.name}")  # False


""""Main Thread / enumerated threads"""

# thread = threading.current_thread()
# identifier = get_native_id()
# print(f"name: {thread.name} daemon: {thread.daemon} "
#       f"id: {thread.ident} Native Id: {identifier}")

"""Enumerate threads"""
# threads = threading.enumerate()
# for thr in threads:
#     print(f"thread-{thr.name}")

"""Thread-Local Data"""

#
# def task(time_to_sleep):
#     local = threading.local()
#     local.value = time_to_sleep
#     time.sleep(time_to_sleep)
#
#     print(f"Time to sleep is: {local.value}")
#
#
# # create and start a thread
# threading.Thread(target=task, args=(1,)).start()
#
# # create and start another thread
#
# threading.Thread(target=task, args=(3,)).start()
# print(f"the name is: {threading.Thread().name}")
# threading.Thread(target=task, args=(4,)).start()
# print(f"the name is: {threading.Thread().name}")
# threading.Thread(target=task, args=(5,)).start()
# print(f"the name is: {threading.Thread().name}")
# threading.Thread(target=task, args=(2,)).start()
# print(f"the name is: {threading.Thread().name}")
# threading.Thread(target=task, args=(2,)).start()
# print(f"the name is: {threading.Thread().name}")
# print(f"Active threads counted: {threading.active_count()}")

"""
------ Reentrant Lock ------

What is a Reentrant Lock?

A reentrant lock is a synchronization primitive that may be acquired multiple times by the 
same thread. In the locked state, some thread owns the lock; in the unlocked state, 
no thread owns it.
"""

#
# def report_thread(lock, id):
#     with lock:
#         print(f"> The Thread {id} is done")
#
#
# def task(lock, identifier, value):
#     with lock:
#         print(f"> The thread {identifier} is sleeping for {value} seconds")
#         time.sleep(value)
#         report_thread(lock, identifier)
#
#
# # Create shared lock
# lock = threading.RLock()
# for i in range(10):
#     threading.Thread(target=task, args=(lock, i, random())).start()
# # threads = threading.enumerate()
# # for thr in threads:
# #     print(f"thread-{thr.name}")
#
# """Thread-Local Data"""
#
#
# def task(time_to_sleep):
#     local = threading.local()
#     local.value = time_to_sleep
#     time.sleep(time_to_sleep)
#
#     print(f"Time to sleep is: {local.value}")
#
#
# # create and start a thread
# threading.Thread(target=task, args=(1,)).start()
#
# # create and start another thread
#
# threading.Thread(target=task, args=(3,)).start()
# print(f"the name is: {threading.Thread().name}")
# threading.Thread(target=task, args=(4,)).start()
# print(f"the name is: {threading.Thread().name}")
# threading.Thread(target=task, args=(5,)).start()
# print(f"the name is: {threading.Thread().name}")
# threading.Thread(target=task, args=(2,)).start()
# print(f"the name is: {threading.Thread().name}")
# threading.Thread(target=task, args=(2,)).start()
# print(f"the name is: {threading.Thread().name}")
# print(f"Active threads counted: {threading.active_count()}")


# SuperFastPython.com
# example of wait/notify with a condition
from threading import Timer


# target task function
def task(message):
    # report the custom message
    print(message)


# create a thread timer object
timer = Timer(3, task, args=('Hello world',))
# start the timer object
timer.start()
# wait for the timer to finish
print('Waiting for the timer...')