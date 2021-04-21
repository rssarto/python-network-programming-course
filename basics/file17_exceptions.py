from log_variable import log_variable

# for in range(10): Has syntax error

# 4 / 0  Throws a ZeroDivisionError

for i in range(5):
    try:
        log_variable("i / 0", i / 0)
    except ZeroDivisionError as err:
        print(err, "--> Division by 0 is not allowed")
        log_variable("i / 0", err)

for i in range(5):
    try:
        log_variable("i / 0", i / 0)
    except:
        print("Error!")

for i in range(5):
    try:
        log_variable("i / 0", i / 0)
    except ZeroDivisionError:
        print("Division by 0 is not allowed")
    except NameError:
        print("Name error detected!")
    except ValueError:
        print("Wrong value")

try:
    print(4 / 2)
except NameError:
    print("Name Error!")
else:
    print("No exceptions raised by the code")  # executed only if no error is thrown in the try block

try:
    print(4 / 0)
except NameError:
    print("Name Error!")
finally:
    print("I don't care, I'm getting printed anyway")  # always executed
