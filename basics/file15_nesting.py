from log_variable import log_variable

x = "Cisco"
if "i" in x:
    if len(x) > 3:
        log_variable("x", x)

if ("i" in x) and (len(x) > 3):
    log_variable("x", x)

list1 = [4, 5, 6]
list2 = [10, 20, 30]
for i in list1:
    for j in list2:
        log_variable("i * j", i * j)
    log_variable("i", i)

x = 1
while x <= 10:
    z = 5
    x += 1
    while z <= 10:
        log_variable("z", z)
        z += 1

for number in range(10):
    if 5 <= number <= 9:
        log_variable("number", number)
