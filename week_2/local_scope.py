#1. Local scope
#Local scope refers to a variable declared inside a function. For example, in the code below, the variable total is only available to the code within the get_total function. Anything outside of this function will not have access to it.
def get_total(a, b):
    #local variable declared inside a function
    total = a + b;
    return total

print(get_total(5, 2))
# Accessing variable outside of the function:
# print(total)
# NameError: name 'total' is not defined
