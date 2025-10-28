"""
write a python program to count the number of times a class is called
or
how to count number of instances of a class in python?
"""
#way1 : using class variable
class A:
  count=0
  def __init__(self):
    A.count+=1
    print("class A is called")
a1=A()
a2=A()
print(A.count)

#way 2 : using global variable
count=0
class B:
  def __init__(self):
    global count
    count+=1
    print("class B is called")
b1=B()
b2=B()
print(count)

#output
"""
class A is called
class A is called
2
class B is called
class B is called
2
"""


