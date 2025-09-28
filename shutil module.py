#shutil module is used for high-level file operations like copying and archiving files and directories.
#copying a file from one location to another location
import shutil

shutil.copy(
    "/Users/tusharchaudhary/Documents/python learning/shutil module.py",
    "/Users/tusharchaudhary/Documents/python learning/shutil module2.py"
)



#copying a directory from one location to another location
import shutil
shutil.copytree(
    "/Users/tusharchaudhary/Documents/python learning",
    "/Users/tusharchaudhary/Documents/python learning2"
)


#moving a file from one location to another location
import shutil
shutil.move(
    "/Users/tusharchaudhary/Documents/python learning/shutil module2.py",
    "/Users/tusharchaudhary/Documents/python learning2/shutil module2.py"

)

#deleting a directory
import shutil
shutil.rmtree("/Users/tusharchaudhary/Documents/python learning2")