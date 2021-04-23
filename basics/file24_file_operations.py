"""
Opening modes:
r - reading (default mode)
w - writing, creates the file if it not exists and replace the if it exists
a - appending, creates the file if it not exists or append data if it exists
b - binary
x - exclusive creation, throws an Error if the file already exists
r+
w+ - Writing and reading at the same time, creates the file if it not exists
a+

reading file methods:
read() - read the entire file content. Useful for searching in the entire file or matching patterns (regex)

references:
https://docs.python.org/3/library/functions.html#open
https://www.tutorialspoint.com/python/python_files_io.htm
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

# Creating a new file - The created file is in writing mode and it cannot be used to read the written content.
new_file = open("./resources/temp/newfile.txt", "w")
new_file.write("I like Python!\nDo you?")
new_file.close()

# Opening the just created file in writing mode, in this case it'll replace the content written above.
new_file = open("./resources/temp/newfile.txt", "w")
new_file.write("This is great")
new_file.close()

new_file_2 = open("./resources/temp/newfile2.txt", "w")
new_file_2.writelines(["Cisco", "Juniper", "HP"])
new_file_2.close()

# Appending information to the file
new_file_2 = open("./resources/temp/newfile2.txt", "a")
new_file_2.write("This string was appended")
new_file_2.close()

# Creating a new file with w+ (writing + reading) mode
new_file_3 = open("./resources/temp/newfile3.txt", "w+")
new_file_3.write("something else")
new_file_3.seek(0)
log_variable("new_file_3.read()", new_file_3.read())
new_file_3.close()

# Checking the file is closed
log_variable("new_file_3.closed", new_file_3.closed)

# Closing the file without calling the close method explicitly.  The 'as' access an assignment operator for the file
with open("./resources/temp/newfile4.txt", "w") as f:
    f.write("Hello Python!!!")
log_variable("f.closed", f.closed)
