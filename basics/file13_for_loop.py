from log_variable import log_variable

vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
for each_vendor in vendors:
    log_variable("each_vendor", each_vendor)

my_string = "Cisco"
for letter in my_string:
    log_variable("letter", letter)
    log_variable("letter * 2", letter * 2)
    log_variable("letter * 3", letter * 3)

range_structure = range(10)
for i in range_structure:
    log_variable("i * 2", i * 2)

for index in range(len(vendors)):
    log_variable(f"vendors[{index}]", vendors[index])

for index, element in enumerate(vendors):
    log_variable("index, element", f"{index}, {element}")

for element in vendors:
    log_variable("element", element)
else:
    log_variable("end of list in loop", True)
