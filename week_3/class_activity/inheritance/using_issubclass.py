"""
The case above is an example of multi-level inheritance where the derived class C inherits from base class B. The class B is in turn a derived class of base class C. Class B here is an intermediary derived class. There are three levels of inheritance in this case, but it could be extended as long as I want, though it may become impractical after a while.
"""
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)
#issubclass(class A, class B)

#print(issubclass(A,B))
#print(issubclass(B,A))
