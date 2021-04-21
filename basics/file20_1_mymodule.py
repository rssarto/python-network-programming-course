"""
The code inside a module is executed once when the module is imported
"""

my_var = 10


def my_funcition():
    print("This is the function inside the module!")


if __name__ == "__main__":  # execute only when executing this code as a standalone application
    print("This will be executed")
