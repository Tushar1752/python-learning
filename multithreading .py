#multithreading is defined as the concurrent execution of more than one sequential set of instructions, or thread. all threads within a process share the same memory space, which allows them to communicate with each other more easily than if they were separate processes. however, this also means that threads can interfere with each other if they try to access the same memory location at the same time, leading to potential data corruption or other issues.  and because threads share the same memory space, they are generally more lightweight and faster to create and manage than separate processes, which have their own memory space and require more overhead to communicate with each other.
import threading
import time
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    print(f"Finished sleeping for {seconds} seconds")
func(4)
#to run the function in a separate thread, we can use the threading module in python.
thread = threading.Thread(target=func, args=(4,))
thread.start()
print("Main thread continues to run while func is sleeping")
#we can also create multiple threads to run the function concurrently.
threads = []
for i in range(5):
    thread = threading.Thread(target=func, args=(i,))
    threads.append(thread)
    thread.start()
#wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads finished")


#simple example of multithreading

import threading
import time
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

time1=time.perf_counter()


t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[1])
t1.start() 
t2.start()
t3.start()
time2=time.perf_counter()
print(f"Time taken to create threads: {time2-time1} seconds")