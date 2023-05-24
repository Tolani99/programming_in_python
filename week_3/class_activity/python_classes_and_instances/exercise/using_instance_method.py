"""
@Payslips - The class Object

The code provided defines a class called Payslips that represents a payslip.
Each instance of the class has attributes such as name, payment, and amount,
representing the employee's name, payment status, and the amount to be paid,
respectively. The class also has methods pay() and status().

In the code, two instances of the Payslips class are created: nathan and roger.
Both instances have their payment attribute set to 'no' initially.

The status() method checks the value of the payment attribute
and returns a string indicating whether the employee is paid or not.

After creating the instances, the code prints the status of both employees
using the status() method. Since the payment attribute is set to 'no' for
both instances, the output will indicate that
neither Nathan nor Roger is paid yet.

Next, the pay() method is called on the nathan instance, which changes
the value of the payment attribute to 'yes',
indicating that Nathan has been paid.
"""

class Payslips:

    """
    @__init__ - A special method used to initialize
                objects of a class
    @pay - A class method
    @status - A class method
    """
    def __init__(self, name, payment, amount) -> None:
        """
        This is a class constructor
        """
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        """
        This is a class method
        """
        self.payment = 'yes'

    def status(self):
        """
        This is a class method
        """
        if self.payment == 'yes':
            return self.name + " is paid " + str(self.amount)
        return self.name + " is not paid yet"

nathan = Payslips("Nathan", "no", 1000)
roger = Payslips("Roger", "no", 3000)

print(nathan.status(), "\n", roger.status())

nathan.pay()
print("After payment")
print(nathan.status(), "\n", roger.status())
