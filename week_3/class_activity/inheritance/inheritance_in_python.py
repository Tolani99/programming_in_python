"""
The Employees class is defined with an __init__ method that takes two parameters: name and last. Inside the method, the name and last values are assigned to the self.name and self.last attributes, respectively.

The Supervisors class is defined as a subclass of Employees using inheritance. It has an additional parameter, password, in its __init__ method. The super().__init__(name, last) statement is used to call the __init__ method of the parent class (Employees) and pass the name and last values to initialize those attributes. The self.password attribute is then assigned the value of the password parameter.

The Chefs class is also a subclass of Employees. It does not have any additional parameters or methods apart from those inherited from the Employees class.

An instance of the Supervisors class named adrain is created, passing the values "Adrain", "A", and "apple" as arguments for the name, last, and password parameters, respectively.

Instances of the Chefs class named emily and juno are created, passing the values "Emily" and "E" for emily, and "Juno" and "J" for juno, corresponding to the name and last parameters.

The code then prints the result of calling the leave_request() method on the emily object, passing the value 3 as the days parameter. It also prints the password attribute of the adrain object and the name attribute of the emily object.
"""
class Employees:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last


class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days"


adrain = Supervisors("Adrain", "A", "apple")

emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

print(emily.leave_request(3))
print(adrain.password)
print(emily.name)
