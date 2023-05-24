"""
Another built-in function similar to this one is isinstance() thatdetermines if some object is an instance of some class. 
"""
Class A:
	pass
Class B(A):
	pass

b = B()
print(isinstance(b,B))
print(isinstance(b,B))

"""
The output that I will get is "True".

Now that you know how classes can be extended from other classes, let's look at another useful built-in function called the super() function.

The super() function is a built-in function that can be called inside the derived class and gives access to the methods and variables of the parent classes or sibling classes. Sibling classes are the classes that share the same parent class. When you call the super() function, you get an object that represents the parent class in return.

The super() function plays an important role in multiple inheritance and helps drive the flow of the code execution. It helps in managing or determining the control of from where I can draw the values of my desired functions and variables.

If you change anything inside the parent class, there is a direct retrieval of changes inside the derived class. This is mainly used in places where you need to initialize the functionalities present inside the parent class in the child class as well. You can then add additional code in the child class.
"""
