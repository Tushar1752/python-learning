#genrator function in python is a function that returns an iterator that produces a sequence of values when iterated over.also it uses the yield statement to return values one at a time, pausing the function's state between each yield, allowing it to be resumed later.and it is more memory efficient than a regular function that returns a list, as it generates values on-the-fly and does not store the entire sequence in memory at once.


def my_generator():
    for i in range(300):
        yield i
gen=my_generator()
print(next(gen))
print(next(gen))
print(next(gen))


#or we can use a for loop to iterate through the generator
def my_generator():
    for i in range(1000):
        yield i
gen=my_generator()
for value in my_generator():
    print(value)