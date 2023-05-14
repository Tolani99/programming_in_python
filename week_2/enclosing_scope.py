"""
2. Enclosing scope
Enclosing scope refers to a function inside another function or what is commonly called a nested function. 

In the code below, I added a nested function called double_it to the get_total function. 

As double_it is inside the scope for the get_total function it can then access the variable. However, the enclosed variable inside the double_it function cannot be accessed from inside the get_total function.
"""
def get_total(a, b):
    
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(double)

    double_it()
    #double variable will not be accessible
    print(double)

    return total
