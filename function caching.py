#function caching is a way to store the results of a function so that if the function is called again with the same arguments, the stored result can be returned instead of recalculating it.
#This can be useful for functions that are computationally expensive or that are called frequently with the same arguments.
#In Python, function caching can be implemented using the functools.lru_cache decorator.    



import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(1) # Simulating a time-consuming computation
    return n*n
print(fx(10))
print("Done for 10")
print(fx(220))
print("Done for 220")
print(fx(20))
print("Done for 20")


#next example

import functools
import time
@functools.lru_cache(maxsize=None)
def fib(n):
     if n<2:
        return n
     return fib(n-1)+fib(n-2)
print(fib(20))
print("Done for 20")
print(fib(30))
print("Done for 30")