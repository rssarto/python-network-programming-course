"""
class - is a data type containing its owm variables, methods and functions
"""
from log_variable import log_variable


# When a class does not inherit from another class then say it inherits from object class
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
