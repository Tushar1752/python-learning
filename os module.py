 #This code creates so many folders easily

import os 
if(not os.path.exists("data")):
   os.mkdir('data')
for i in range (0,100):
    os.mkdir(f"Data/Day{i+1}")


#rename the folders created from day to tutorial
import os
for i in range(0,100):
    os.rename(f"data/Day{i+1}", f"data/Tutorial {i+1}")  

#to check which which folder are created
import os
folders= os.listdir("data")
print(folders) # This will print the list of folders created in the 'data'

#To print folders created inside the folders

import os
for folder in folders:
    print(folders)
    print(os.listdir(f"data/{folder}")) # This will print the contents of each folder in 'data'