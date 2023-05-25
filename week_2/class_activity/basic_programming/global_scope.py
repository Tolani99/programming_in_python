"""
3. Global scope
Global scope is when a variable is declared outside of a function. This means it can be accessed from anywhere.

In the code below, I  added a global variable called special. This can then be accessed from both functions get_total and double_it:
"""

special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #local variable
        double = total * 2
        print(special)

    double_it()

    return total
