#multiprocessing is defined as a package that supports spawning processes using an API similar to the threading module.and it offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. also offers the same interface as the threading module.

#downloading multiple files using multiprocessing
import multiprocessing
import requests

def download_file(url,name):
    response = requests.get(url)
    open(f"{name}.jpg","wb").write(response.content)
url="https://picsum.photos/2000/3000"
for i in range(5):
    download_file(url,i)



#multitprocessing.process is used to create a new process
import multiprocessing
import requests
def download_file(url,name):
    response = requests.get(url)
    open(f"{name}.jpg","wb").write(response.content)
url="https://picsum.photos/2000/3000"
for i in range(5):
    process = multiprocessing.Process(target=download_file,args=(url,i))
    process.start()
    process.append(process)  #wait for the process to finish before starting the next one
for p in process:
    p.join()