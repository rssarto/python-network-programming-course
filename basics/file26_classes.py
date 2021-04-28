"""
class - is a data type containing its owm variables, methods and functions
"""
from log_variable import log_variable

"""
When a class does not inherit from another class then say it inherits from object class
Multiple inheritance is allowed. Class definition example: class MyRouter(Parent1, Parent2, Parent3):
"""


class MyRouter(object):
    "This is a class that describes the characteristics of a router."

    # class constructor
    def __init__(self, routername, model, serialno, ios):
        # instance variables
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is:", self.model)
        print("The serial number of:", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)


router1 = MyRouter("R1", "2600", "123456", "12.4")
log_variable("router1", router1)
log_variable("router1.model", router1.model)
log_variable("router1.ios", router1.ios)
log_variable("router1.serialno", router1.serialno)
log_variable("router1.routername", router1.routername)

router1.print_router("20181010")
log_variable("getattr(router1, \"ios\")", getattr(router1, "ios"))
setattr(router1, "ios", "13.1")
log_variable("getattr(router1, \"ios\")", getattr(router1, "ios"))
log_variable("hasattr(router1, \"ios\")", hasattr(router1, "ios"))
log_variable("hasattr(router1, \"ios2\")", hasattr(router1, "ios2"))
delattr(router1, "ios")
log_variable("hasattr(router1, \"ios\")", hasattr(router1, "ios"))
try:
    log_variable("getattr(router1, \"ios\")", getattr(router1, "ios"))
except AttributeError as err:
    log_variable("err", err)


# Inheritance
class MyNewRouter(MyRouter):
    # redefining the constructor
    def __init__(self, routername, model, serialno, ios, portsno):
        MyRouter.__init__(self, routername, model, serialno, ios)
        self.portsno = portsno

    def print_new_router(self, string):
        print(string + self.model)


new_router1 = MyNewRouter("newr1", "1800", "111111", "12.2", "10")
new_router1.print_new_router("child router 1")
new_router1.print_router("chnnl")

log_variable("new_router1.portsno", new_router1.portsno)

# retrieving parent's properties values using child instance
log_variable("new_router1.model", new_router1.model)
log_variable("new_router1.ios", new_router1.ios)
log_variable("new_router1.serialno", new_router1.serialno)
log_variable("new_router1.routername", new_router1.routername)

# Checking a class is a subclass of another class
log_variable("issubclass(MyNewRouter, MyRouter)", issubclass(MyNewRouter, MyRouter))
log_variable("issubclass(MyNewRouter, object)", issubclass(MyNewRouter, object))
log_variable("issubclass(MyNewRouter, int)", issubclass(MyNewRouter, int))
