"""
COPY OPERATION 

--> It is phenomenon of copying a context , from one variable to another variable.

--> It is of 3 types , they are : 1) General / Normal copy
                                  2) Shallow copy
                                  3) Deep copy

1) General/Normal copy :

--> It is phenomenon of copying a context , from one variable to another variable
    to the same memory location.

--> When a mutable collection is modified , it effects another variable also (drawback).

--> General copy can be done on all the datatypes, but modification will work only
    on mutable datatypes.


Syntax : dest_var = source_var
"""
#Example : 

a=10
b=a
b
10

id(a)
140723140119256
id(b)
140723140119256

x=[10,20,30]
y=x
y
[10, 20, 30]

y[0]=777

y
[777, 20, 30]
x
[777, 20, 30]

"""
2) Shallow copy :

--> It is phenomenon of copying a context , from one variable to another variable
    to the different memory location.

Syntax : dest_var = source_var.copy()

NOTE : 

1) It works only on mutable datatypes
2) In case of Nested collection , it copies to the same memory location (drawback).
3) If a nested collection is modified with respect to one variable , it will 
   affect other variable also.
"""
#Example : 

x=[1.5,22,[1,2,3]]
y=x.copy()
y
[1.5, 22, [1, 2, 3]]

x[2][0]=777
x
[1.5, 22, [777, 2, 3]]
y
[1.5, 22, [777, 2, 3]]

id(x)
2168249701120
id(y)
2168292643648

id(x[-1])
2168292710848
id(y[-1])
2168292710848
"""
3) Deep copy :

--> It is a phenomenon of copying the context from one variable to another 
    variable to the different memory location.

--> If there are nested collection then also, it copies to the different 
    memory location.

Syntax : import copy
         dest_var = copy.deepcopy(source_var)
"""
#Example : 

a=[10,20,[7,8]]
import copy
b=copy.deepcopy(a)
b
[10, 20, [7, 8]]

a[2][0]=99.99
a
[10, 20, [99.99, 8]]
b
[10, 20, [7, 8]]

id(a)
1163485900416
id(b)
1163491415552

id(a[2])
1163491348608
id(b[2])
1163447489280
