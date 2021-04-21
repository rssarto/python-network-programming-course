from log_variable import log_variable

for number in range(10):
    if number == 7:
        break
    log_variable("number", number)

list1 = [4, 5, 6]
list2 = [10, 20, 30]
for i in list1:
    for j in list2:
        if j == 20:
            break
        log_variable("i * j", i * j)
    print("Outside the nested loop")

for i in list1:
    for j in list2:
        if j == 20:
            continue
        log_variable("i * j", i * j)
    print("Outside the nested loop")

for i in range(10):
    pass  # used for incomplete parts of your code
