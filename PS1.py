# 1. Write a Program to Print a poem in Python.
print("It name means two things, but who could thought it will be that useful,")
print("One was scary and no one wanted to go near but other was always coming up,")
print("It was easy to understand, everyone were cheerful after meeting that,")
print("Python is no more the name of some outrageous animal, it's now intelligence human have grabbed.")

# 2.Use REPL and Print the table of 5 using it.

# 3.Install an External Module and use it to perform an operation of your interest.
import numpy as np

arr = np.array((1,2,3,4,5))
print(arr)
# 4.Write a Python Program to print the contents of a directory using OS Module. Search Online for the function which does that.
import os
 
# Get the list of all files and directories
path = "A:\Books In PDF"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)
# 5.Label the Program written in the Problem 4 with comments.
