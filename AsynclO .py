#asynchronous I/O is a programming paradigm that allows for non-blocking operations, enabling other tasks to run while waiting for I/O operations to complete. also known as async I/O or non-blocking I/O, it is commonly used in scenarios where applications need to handle multiple tasks concurrently, such as web servers, network applications, and real-time data processing.       

#Syntax:
import asyncio

async def my_async_function():
    await asyncio.sleep(10)
    return "Hello, Async World!"

async def main():
    result = await my_async_function()  # single line
    print(result)

asyncio.run(main())


#Output: Hello, Async World!

#In this example, my_async_function is defined as an asynchronous function using the async keyword. It simulates a non-blocking operation by awaiting asyncio.sleep(10), which pauses the function for 10 seconds without blocking the event loop. The main function calls my_async_function and awaits its result, printing "Hello, Async World!" once the operation is complete. The asyncio.run(main()) function is used to execute the main coroutine.  


#next example:

import time
import asyncio
import requests

async def function1():
    print("Function 1 started")
    URL = "https://www.istockphoto.com/photo/scenic-aerial-view-of-the-mountain-landscape-with-a-forest-and-the-crystal-blue-gm1458782106-493292590"
    response = requests.get(URL)
    open("image1.jpg", "wb").write(response.content)
    print("Function 1 completed")

async def function2():
    print("Function 2 started")
    URL="https://unsplash.com/photos/blooming-tree-blossoms-against-a-bright-blue-sky-gnDmwo2QE_w"
    response = requests.get(URL)
    open("image2.jpg", "wb").write(response.content)
    print("Function 2 completed")

async def function3():
    print("Function 3 started")
    URL="https://unsplash.com/photos/red-tulips-bloom-beautifully-in-the-spring-garden-cmzZU6zFvto"
    response=requests.get(URL)
    open("image3.jpg","wb").write(response.content)
    print("Function 3 completed")

async def main():
    L= await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)
asyncio.run(main())