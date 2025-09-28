#WAP to rename all the files in a folder with a number starting from 1.

import os 
files=os.listdir("clutterd Folder")
i=1
for file in files:
    if file.endswidth(".txt"):
        os.rename(f"cluttered Folder/{file}",f"clutterd Folder/{i}.txt")
        i=i+1