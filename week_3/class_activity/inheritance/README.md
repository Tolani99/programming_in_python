Inheritance
Inheritance in Python will be covered later in the course.
As the structure of inheritance gets more complicated, Python adheres to something called the Method Resolution Order (MRO) that determines the flow of execution. MRO is a set of rules, or an algorithm, that Python uses to implement monotonicity, which refers to the order or sequence in which the interpreter will look for the variables and functions to implement. This also helps in determining the scope of the different members of the given class.
Let’s say there two classes, namely class A and class B. If you have to perform simple inheritance, it can be done as follows:
Class A:

    pass

Class B(A):

    pass

# Multiple inheritance
You have learned about single inheritance so far, but Python also gives us the ability to perform multiple inheritance between classes.

# Example 1
class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)

First, two classes called A and B are created and then variables a and b respectively are initialized with values. A new class C is then defined and classes A and B are passed to it. This is how multiple inheritance is done in Python. The order of classes is important, but not in this specific example. I then instantiate an object ‘c’ of class C. The values of the a and b variables are printed over the object c of class C even though a and b are not present inside class C.

The code above is an example of multiple inheritance. There are also other types of inheritance that fall under the umbrella of multiple inheritance. Let's examine an example.

# Multi-level inheritance
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)

The output is 2 because C derives from the immediate super class of C, and that's B.
The case above is an example of multi-level inheritance where the derived class C inherits from base class B. The class B is in turn a derived class of base class C. Class B here is an intermediary derived class. There are three levels of inheritance in this case, but it could be extended as long as I want, though it may become impractical after a while.

