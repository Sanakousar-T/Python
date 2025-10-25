"""
05) ASSIGNMENT OPERATORS :

--> It is an operator which is used to assign a value to a variable (=).

Argumented assignment operator  :->
-------------------------------------

--> Whenever a variable has to be updated these operators will be used.
--> It increses the efficiency by simplifying it.
--> It works for Arithmetic and Bitwise operators.

a = a+b   -->   a += b                a = a&b  -->   a &= b
a = a-b   -->   a -= b                a = a|b  -->   a |= b
a = a*b   -->   a *= b                a = a^b  -->   a ^= b
a = a/b   -->   a /= b                a = a<<b  -->   a <<= b
a = a//b  -->   a //= b               a = a>>b  -->   a >>= b
a = a%b   -->   a %= b
a = a**b  -->   a **= b 
"""
#EXAMPLE :

a=10
b=20
a+=b
a
30

x=70
y=65
x-=y
x
5

a=10
b=21
a&=b
a
0

x=7
y=3
x^=y
x
4	

"""
06) Membership operator :->
-------------------------
--> It is an opearator which checks whether the value is present in a 
    collection or not.

--> This operator is applicable only for collection datatype.

--> It is of 2 types :  1) in operator
                        2) not in operator
1) in operator : 
------------------
--> It is an operator which gives result as true if the value is present
    in the collection.

Syntax : val in collection
"""
#Example : 

3 in [1,2,3,4.5]
True
[1,2] in [1,2,3]
False
[1,2] in [[1,2],3,4,5]
True

5 in 4567   ----> Error
5 in '4567' ----> Error

'5' in '4567'
True

"""
2) not in operator : 
--------------------
--> It is an operator which gives result as true if the value is not present
    in the collection.

Syntax : val in collection
"""
#EXAMPLE :

1.25 not in ([1.25],2,777)
True
45 not in [1,2,3]
True
123 not in [1,1.23,(123),123.1]
False
123 not in [1,1.23,(123,),123.1]
True

"""
07) Identity operator :-
------------------------
--> It is an operator which checks whether the values are pointing  towards same memory location or not.

--> It is of 2 types :-> 1) is operator 
                         2) is not operator
1) is operator : 
---------------
--> It is an operator which gives us result as true, if the values are pointing towards same memory location.

Syntax :  val1 is val2
"""
#Examples:

a=10
b=a
b
10
a is b
True
c=3
a is c
False
import copy
x=[1,2,3]
d=copy.deepcopy(x)
d
[1, 2, 3]
x is d
False 

"""
2) is not operator :
--------------------
--> It is an operator which gives us result as true, if the values are not pointing towards same memory location.

Syntax : val1 is not val2
"""
#EXAMPLE: 

a=1
b=2
c=[1,2.5]
d=c.copy()
d
[1, 2.5]
c is not d
True
a is not b
True
z=a
a is not z
False
