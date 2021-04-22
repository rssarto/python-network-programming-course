"""
Opening modes:
r - reading (default mode)
w - writing
a - appending
b - binary
x - exclusive creation, throws an Error if the file already exists

reading file methods:
read() - read the entire file content. Useful for searching in the entire file or matching patterns (regex)
"""
from log_variable import log_variable

myfile = open("./resources/routers.txt", "r")
log_variable("myfile", myfile)

# Reads the entire file content and position the cursor at the end of the file
log_variable("myfile.read()", myfile.read())

# Reading specific line
myfile.seek(0)  # Position the cursor at the beginning of the file
myfile.tell()  # Shows the cursor current position
log_variable("myfile.read()", myfile.read(5))

# Reading line by line
myfile.seek(0)
log_variable("myfile.readline()", myfile.readline())

# Reading and converting all the lines in a list
myfile.seek(0)
for vendor in myfile.readlines():
    if vendor[0] == "A":
        log_variable("vendor", vendor)

